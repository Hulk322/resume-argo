# coding=utf-8
"""
Copyright © 2021 U.S. TECH SOLUTIONS LICENSE

@version 0.2.0
Resume Normalization Client
@author <ankits@simplifyvms.com>
"""
import threading
import time
import json
import datetime
import itertools
from starlette import status
import utils
import asyncio
import nest_asyncio
import aiohttp
#import config
import config as config

from utils import normalize_resume_titles, create_edu_object, normalize_education_data,\
        normalize_skills, normalize_location, normalize_industry, normalize_job_types, \
        merge_industry, categorise_skills, pick_industries_lies_in_k_percent_of_max

from logger import standardLogger

rnc_logger = standardLogger().get_logger("Resume Normalization Client Logger")
nest_asyncio.apply()

class ResumeNorm:
    def __init__(self):

        self.titles = []
        self.socCode = []
        self.work_ex_experiences = []

    def normalize_resume(self, pars_resp):
        result = {}
        time_logs = {}
        try:
            result['temp'] = {}
            ts0 = time.time()
            self.work_ex_experiences = self.fetch_all_work_ex_durations(pars_resp)
            self.re_compute_overall_exp(pars_resp)
            ts1 = time.time()
            time_logs['work_exp'] = (ts1 - ts0)

            result[config.NORM_EXPERIENCE_FIELD] = self.update_skills_cumulative(pars_resp)
            time_logs['exp'] = (time.time() - ts1)

            t6 = threading.Thread(target=self.update_education,
                                  args=(pars_resp, result, config.NORM_EDUCATION_FIELD,))
            t6.start()
            #result[config.NORM_EDUCATION_FIELD] = t6.start()

            t7 = threading.Thread(target=self.update_location,
                                  args=(pars_resp, result, config.NORM_LOCATION_FIELD,))
            t7.start()
            #result[config.NORM_LOCATION_FIELD] = t7.start()

            t8 = threading.Thread(target=self.update_title,
                                  args=(pars_resp, result, config.NORM_TITLE_FIELD,))
            t8.start()
            #result[config.NORM_TITLE_FIELD] = t8.start()

            skills = {'temp': {}}
            ts2 = time.time()
            t1 = threading.Thread(target=self.update_domain_skills,
                                  args=(pars_resp, skills, 'domain_skills',))
            t1.start()

            cumul_skills_param = list(
                map(lambda k: k[config.SKILL_EXP_NAME_FIELD],
                    result.get(config.NORM_EXPERIENCE_FIELD, {}).get(
                        config.SKILL_WISE_EXPERIENCE_FIELD, [])))
            t2 = threading.Thread(target=self.update_cumulative_skills,
                                  args=(cumul_skills_param, skills, 'cumulative_skills',))
            t2.start()

            t3 = threading.Thread(target=self.update_common_skills,
                                  args=(pars_resp, skills, 'common_skills',))
            t3.start()

            t1.join()
            t2.join()
            t3.join()
            domain_skills = skills.get('domain_skills')
            cumulative_skills = skills.get('cumulative_skills')
            common_skills = skills.get('common_skills')
            time_logs['skills'] = (time.time() - ts2)
            print('skills: {} {}'.format(domain_skills, type(domain_skills)))

            st = time.time()
            t4 = threading.Thread(target=categorise_skills,
                                  args=(list(set(domain_skills + cumulative_skills)),
                                        skills, 'categorized_skills',))
            t4.start()
            t4.join()
            categorized_skills = skills.get('categorized_skills')
            time_logs['skills - categorization'] = skills['temp']['skills - categorization']

            result[config.NORM_SKILLS_FIELD] = {
                config.NORMALIZED_COMMON_SKILLS_FIELD:
                common_skills,
                config.NORMALIZED_SKILLS_FIELD:
                list(set(domain_skills + cumulative_skills)),
                config.INDUSTRY_CLF_API_INDUSTRY_WISE_SKILLS_FIELD:
                categorized_skills
            }

            ts3 = time.time()
            st = time.time()
            industry = self.update_industry(pars_resp)
            result[config.NORM_INDUSTRY_FIELD] = merge_industry(industry, self.work_ex_experiences)

            time_logs['industry - work experience industries'] = time.time() - st

            st = time.time()
            result[config.
                   OVERALL_NORM_INDUSTRY_FIELD] = self.update_overall_industry(
                       pars_resp, cumulative_skills, domain_skills, common_skills)
            time_logs['industry - overall industries'] = time.time() - st

            ts4 = time.time()
            time_logs['industry'] = (ts4 - ts3)

            result[config.NORM_JOB_TYPE_FIELD] = self.update_job_types(
                pars_resp)
            result[config.MANAGEMENT_LEVEL_FIELD] = pars_resp.get(
                config.MANAGEMENT_LEVEL_FIELD)
            result[config.NORM_CERT_FIELD] = pars_resp.get("parsed_resume", {}).get("data", {}).get("certification", [])
            ts5 = time.time()
            time_logs['job_type'] = (ts5 - ts4)

            t6.join()
            t7.join()
            t8.join()
            time_logs['edu'] = result['temp']['edu']
            time_logs['location'] = result['temp']['location']
            time_logs['title'] = result['temp']['title']

            ts9 = time.time()
            time_logs['total'] = (ts9 - ts1)
            rnc_logger.info('Time Logs: {}'.format(time_logs))
            result.pop('temp', {}) #remove temp data
            return {
                'code': status.HTTP_200_OK,
                'message': 'Resume Normalization Successful',
                'timeLogs': time_logs,
                'data': result
            }
        except Exception as e:
            import traceback
            traceback.print_exc()
            rnc_logger.error("ERROR in Resume Normalization: {}".format(e))
            result = {
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': "ERROR in Resume Normalization: {}".format(e)
            }
            return result

    def re_compute_overall_exp(self, elem):
        overall_exp_parsed = elem.get("parsed_resume", {}).get("data", {}).get(
            'total_experience (in months)', 0)
        overall_exp_computed = 0
        lfrom = datetime.datetime.today()
        for wx in sorted(
                self.work_ex_experiences,
                key=lambda k: (k['from'], k['to']),
                reverse=True):
            if wx['to']:
                if wx['to'] < lfrom:
                    overall_exp_computed += wx["durationInMonths"]
        if "parsed_resume" not in elem:
            elem["parsed_resume"] = {}
        if "data" not in elem["parsed_resume"]:
            elem["parsed_resume"]["data"] = {}
        elem["parsed_resume"]["data"]['total_experience (in months)'] = max(
            overall_exp_computed, overall_exp_parsed)

    def update_title(self, elem, result: dict, key: str):
        rnc_logger.info("Start title norm")
        norm_data = None
        st = time.time()
        try:
            experiences = elem.get("parsed_resume", {}).get("data", {}).get(
                "experience", [])
            if experiences:
                titles = []
                for i in experiences:
                    if len(i.get(config.RESUME_TITLE_FIELD_IN_RESUMES)) > 0:
                        for j in i.get(config.RESUME_TITLE_FIELD_IN_RESUMES):
                            titles.append(j.strip())
                    if i.get("sub_experience"):
                        for j in i.get("sub_experience"):
                            if len(j.get(config.RESUME_TITLE_FIELD_IN_RESUMES)) > 0:
                                for k in j.get(config.RESUME_TITLE_FIELD_IN_RESUMES):
                                    titles.append(k.strip())
                # titles = itertools.chain.from_iterable([
                #     x[config.RESUME_TITLE_FIELD_IN_RESUMES]
                #     for x in experiences
                #     if config.RESUME_TITLE_FIELD_IN_RESUMES in x
                # ])
                # titles = [x for x in titles if x and x.strip()]
                self.titles = titles
            else:
                titles = []
            if titles:
                norm_data = normalize_resume_titles(titles)
        except Exception as e:
            rnc_logger.error(
                "ERROR in Normalizing Resume Title : {}".format(e))
        #elem[config.NORM_TITLE_FIELD] = norm_data
        result['temp']['title'] = time.time() - st
        result[key] = norm_data
        return norm_data

    def update_education(self, elem, result: dict, key: str):
        rnc_logger.info("Start education norm")
        educations = elem.get("parsed_resume", {}).get("data", {}).\
            get("education",[])
        norm_data = []
        norm_education = []
        st = time.time()

        try:
            for edu in educations:

                major = edu.get(config.MAJOR_FIELD_IN_JOBS)
                degree = edu.get(config.DEGREE_FIELD_IN_JOBS)
                #univ = edu.get('univ')
                #edu_object = create_edu_object(major=major, degree=degree, school=univ)
                edu_object = create_edu_object(major=major, degree=degree)
                rnc_logger.info("All education data pass to Educaton object %s"
                                % edu_object)
                norm_data.extend(edu_object)

            if norm_data:
                rnc_logger.info("Norm education1 data is %s" % norm_data)
                norm_education = normalize_education_data(norm_data)
                rnc_logger.info("Norm education data is %s" % norm_education)

        except Exception as e:
            rnc_logger.error(
                "ERROR in Normalizing Education Processing: {}".format(e))
        #elem[config.NORM_EDUCATION_FIELD] = norm_education
        result['temp']['edu'] = time.time() - st
        result[key] = norm_education
        return norm_education

    def update_cumulative_skills(self, cumulative_skills, result: dict, key: str):
        rnc_logger.info("Start cumulative skills norm")
        norm_cumulative_skill = []
        try:
            if cumulative_skills:
                norm_cumulative_skill = normalize_skills(cumulative_skills)
                #rnc_logger.info("Norm domain skill  data is %s" % norm_domain_skill)

        except Exception as e:
            rnc_logger.error(
                "ERROR in Normalizing update_cumulative_skills Processing: {}".
                format(e))
        result[key] = norm_cumulative_skill
        return norm_cumulative_skill

    def update_domain_skills(self, elem, result: dict, key: str):
        rnc_logger.info("Start skills norm")
        domain_skills = elem.get("parsed_resume", {}).get("data", {}).\
            get("domain_skills",[])
        norm_domain_skill = []
        try:
            if domain_skills:
                norm_domain_skill = normalize_skills(domain_skills)
                #rnc_logger.info("Norm domain skill  data is %s" % norm_domain_skill)

        except Exception as e:
            rnc_logger.error(
                "ERROR in Normalizing update_domain_skills Processing: {}".
                format(e))
        elem[config.NORMALIZED_SKILLS_FIELD] = norm_domain_skill
        result[key] = norm_domain_skill
        return norm_domain_skill

    def update_common_skills(self, elem, result: dict, key: str):
        rnc_logger.info("Start common skills norm")
        common_skills = elem.get("parsed_resume", {}).get("data", {}).\
            get("common_skills",[])
        norm_common_skill = []
        try:
            if common_skills:
                norm_common_skill = normalize_skills(common_skills)
                #rnc_logger.info("Norm common skill  data is %s" % norm_common_skill)

        except Exception as e:
            rnc_logger.error(
                "ERROR in Normalizing update_common_skills Processing: {}".
                format(e))
        elem[config.NORMALIZED_COMMON_SKILLS_FIELD] = norm_common_skill
        result[key] = norm_common_skill
        return norm_common_skill

    def update_location(self, elem, result: dict, key: str):
        rnc_logger.info("Start location norm")
        address = elem.get("parsed_resume", {}).get("data", {}).get("personal details",{}).\
            get("address",{}).get("formatted_address",{})
        norm_address = []
        st = time.time()
        try:
            if address:
                add = address.get("address", "")
                city = address.get("city/district/county", "")
                state = address.get("state", "")
                country = address.get("country", "")
                norm_address = normalize_location(
                    location=add, city=city, state=state, country=country)

                rnc_logger.info("Norm address  data is %s" % norm_address)

        except Exception as e:
            rnc_logger.error(
                "ERROR in Normalizing update_location Processing: {}".format(
                    e))
        #elem[config.NORM_LOCATION_FIELD] = norm_address
        result['temp']['location'] = time.time() - st
        result[key] = norm_address
        return norm_address

    def update_overall_industry(self,
                                elem,
                                cumulative_skills=[],
                                domain_skills=[],
                                common_skills=[]):
        experience = elem.get("parsed_resume", {}).get("data", {}).\
            get("experience",[])
        main_industry = []
        try:
            if experience:
                exp = experience[0]
                title = exp.get('role', [])
                if title:
                    title = title[0]
                else:
                    title = ""
                main_industry = pick_industries_lies_in_k_percent_of_max(
                    normalize_industry([{
                        config.INDUSTRY_CLF_API_JOB_TITLE_FIELD:
                        title,
                        config.INDUSTRY_CLF_API_SKILLS_FIELD:
                        cumulative_skills * 2 + domain_skills,
                        config.INDUSTRY_CLF_API_COMMON_SKILLS_FIELD:
                        common_skills
                    }])[0])
                rnc_logger.info(
                    "Norm update_overall_industry  data is {}".format(
                        main_industry))
        except Exception as e:
            rnc_logger.error(
                "ERROR in Normalizing update_overall_industry Processing: {}".
                format(e))
        elem[config.OVERALL_NORM_INDUSTRY_FIELD] = main_industry
        return main_industry

    def update_industry(self, elem):
        rnc_logger.info("Start industry norm")
        experience = elem.get("parsed_resume", {}).get("data", {}).\
            get("experience",[])
        main_industry = []
        try:
            if experience:
                #titles = self.titles
                #rnc_logger.info("Titles in update industry method : %s" % titles)
                industries = []
                for exp in experience:
                    title = exp.get('role', [])
                    #if isinstance(title,list) and title:
                    if title:
                        title = title[0]
                    else:
                        title = ""

                    skills = exp.get('skills', [])
                    all_skills = []
                    for skill in skills:

                        skill_name = skill.get('skills_name')

                        all_skills.append(skill_name)
                    industries.append({
                        config.INDUSTRY_CLF_API_JOB_TITLE_FIELD:
                        title,
                        config.INDUSTRY_CLF_API_SKILLS_FIELD:
                        all_skills
                    })

                main_industry = normalize_industry(industries)
                rnc_logger.info(
                    "Norm norm_industry  data is {}".format(main_industry))
                #norm_industry.update({ "title" : title[0] })
                rnc_logger.info(
                    "Type of norm industry in update industry method : {}".
                    format(type(main_industry)))
                for x in main_industry:
                    if x:
                        self.socCode.append(x[0].get('socCode'))
                    else:
                        self.socCode.append("")
        except Exception as e:
            rnc_logger.error(
                "ERROR in Normalizing update_industry Processing: {}".format(
                    e))
        #elem[config.NORM_INDUSTRY_FIELD] = main_industry
        return main_industry

    def parse_exp_date(self, text):
        result = None
        #from_date = text.get('from','')

        if text:
            if text.lower() == "present":
                result = datetime.datetime.today()
                return result
            date_parts = text.split('/')
            if len(date_parts) == 3 and '' not in date_parts:
                if int(date_parts[1]) > 12:
                    result = datetime.datetime(
                        int(date_parts[2]), int(date_parts[0]),
                        int(date_parts[1]), 1)
                else:
                    result = datetime.datetime(
                        int(date_parts[2]), int(date_parts[1]),
                        int(date_parts[0]), 1)
            elif len(date_parts) == 2 and '' not in date_parts:
                result = datetime.datetime(
                    int(date_parts[1]), int(date_parts[0]), 1)
            elif len(date_parts) == 1 and '' not in date_parts:
                result = datetime.datetime(int(date_parts[0]), 1, 1)
            else:
                rnc_logger.error("invalid date format")
        return result

    def fetch_all_work_ex_durations(self, elem):
        rnc_logger.info("Start job type norm")
        experience = elem.get("parsed_resume", {}).get("data", {}). \
            get("experience", [])

        work_ex_experiences = []
        for i, item in enumerate(experience):
            from_date = self.parse_exp_date(item.get('from', ''))
            to_date = self.parse_exp_date(item.get('to', ''))
            print('from:', [item.get('from', ''), from_date])
            print('to:', [item.get('to', ''), to_date])

            if from_date and to_date:
                num_months = abs((to_date.year - from_date.year) * 12 +
                                 (to_date.month - from_date.month))
                rnc_logger.info("Num of months %s in iteration %s" %
                                (num_months, i))
            else:
                num_months = 0
                rnc_logger.error(
                    "Error in Normalizing months calculation %s" % num_months)
            work_ex_experiences.append({
                "from":
                from_date,
                "to":
                to_date,
                "durationInMonths":
                num_months,
                "durationInYears":
                round(num_months / 12, 1)
            })
        return work_ex_experiences

    def update_job_types(self, elem):
        rnc_logger.info("Start job type norm")
        experience = elem.get("parsed_resume", {}).get("data", {}). \
            get("experience", [])
        overall_exp = elem.get("parsed_resume", {}).get("data", {}).get(
            'total_experience (in months)', 0)
        overall_exp = round(overall_exp / 12, 1)
        rnc_logger.info("overall_exp update_job_types {}".format(overall_exp))
        main_job_type = []
        input_job_type_api =[]
        try:
            for i, item in enumerate(experience):
                title = item.get('role', [])
                if title:
                    title = title[0]
                else:
                    title = ""
                experiences = str(overall_exp) + " years of experience"
                overall_exp -= self.work_ex_experiences[i][
                    "durationInYears"] if len(
                        self.work_ex_experiences) > i else 0
                soc_code = self.socCode[i]
                job_type_desc = item.get('description', "")
                rnc_logger.info(
                    "Normalize jobs: For experience %s the Title %s" % (i,
                                                                        title))
                rnc_logger.info(
                    "Normalize jobs: For experience %s the experiences %s" %
                    (i, experiences))
                rnc_logger.info(
                    "Normalize jobs: For experience %s the soc_code %s" %
                    (i, soc_code))
                #rnc_logger.info("Normalize jobs: For experience %s the job_type_desc %s" % (i, job_type_desc))
                input_job_type_api.append((title,[experiences],soc_code,job_type_desc))

            loop = asyncio.new_event_loop()
            main_job_type = loop.run_until_complete(utils.job_type_async(input_job_type_api))
            loop.close()
            job_type_norm = normalize_job_types(
                title=title,
                experience_texts=[experiences],
                soc_code=soc_code,
                job_type=job_type_desc)

            rnc_logger.info("job_type from norm api %s" % job_type_norm)
            #main_job_type.append(job_type_norm)
        except Exception as e:
            rnc_logger.error(
                "ERROR in Normalizing Job Type Processing: {}".format(e))
        #elem[config.NORM_JOB_TYPE_FIELD] = main_job_type

        management_flag = False
        management_exp = 0
        last_exp = 0
        rnc_logger.info("main_job_type from norm api %s" % main_job_type)
        for job_type_obj in sorted(
                main_job_type,
                key=
                lambda k: k.get(config.JOB_TYPE_API_RESPONSE_EXPERIENCE_COUNT_FIELD,0)
        ):
            rnc_logger.info("job_type_obj from norm api %s" % job_type_obj)
            if job_type_obj.get(config.JOB_TYPE_API_RESPONSE_JOB_ROLE_FIELD
                                ) in config.MANAGEMENT_LEVEL_FROM_JOB_ROLES:
                management_exp += (job_type_obj.get(
                    config.JOB_TYPE_API_RESPONSE_EXPERIENCE_COUNT_FIELD) -
                                   last_exp)
                management_flag = True
            last_exp = job_type_obj.get(
                config.JOB_TYPE_API_RESPONSE_EXPERIENCE_COUNT_FIELD)

        management_level = None
        rnc_logger.info("management_flag from norm api %s" % management_flag)
        if management_flag:
            for k, v in config.EXPERIENCE_WISE_MANAGEMENT_LEVELS.items():
                if k[0] <= management_exp < k[1]:
                    management_level = v
                    break

        elem[config.MANAGEMENT_LEVEL_FIELD] = management_level
        rnc_logger.info("Final main_job_type from norm api %s" % main_job_type)
        return main_job_type

    def update_skills_cumulative(self, elem):
        rnc_logger.info("Start experience norm")
        domain_skills_cumulative = elem.get("parsed_resume", {}).get("data", {}). \
            get("skills_cumulative_exp", {}).get("domain_skills",[])
        common_skills_cumulative = elem.get("parsed_resume", {}).get("data", {}). \
            get("skills_cumulative_exp", {}).get("common_skills", [])
        final_output = {}
        try:
            overall_exp = {
                config.SKILL_EXP_COUNT_FIELD:
                "TOTAL",
                "total_months":
                elem.get("parsed_resume", {}).get("data", {}).get(
                    'total_experience (in months)', 0)
            }
            domain_skill_exp = [{
                config.SKILL_EXP_NAME_FIELD:
                item['skills_name'],
                config.SKILL_EXP_COUNT_FIELD:
                "TOTAL",
                "total_months":
                item['totalMonths'],
                config.SKILL_EXP_LAST_USED_FIELD:
                item['LastUsed']
            } for item in domain_skills_cumulative]

            common_skill_exp = [{
                config.SKILL_EXP_NAME_FIELD:
                item['skills_name'],
                config.SKILL_EXP_COUNT_FIELD:
                item['totalMonths'],
                config.SKILL_EXP_LAST_USED_FIELD:
                item['LastUsed']
            } for item in common_skills_cumulative]

            final_output.update({
                config.OVERALL_EXPERIENCE_FIELD:
                overall_exp,
                config.SKILL_WISE_EXPERIENCE_FIELD:
                domain_skill_exp
            })
        except Exception as e:
            rnc_logger.error(
                "ERROR in Normalizing Experience Processing: {}".format(e))
        #elem[config.NORM_EXPERIENCE_FIELD] = final_output
        return final_output
