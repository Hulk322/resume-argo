import os

USE_DOCUMENTDB = False
PARSED_JOBS_COLLECTION = "jobs"
PARSED_RESUMES_COLLECTION = "resumes"

if USE_DOCUMENTDB:
    from documentdb_conf import read_secrets_manager
    #Secret Manager detais
    REGION_NAME = os.get_env("REGION_NAME")#"us-east-1"
    DOCDB_SECRET_NAME = os.get_env("SECRET_NAME")
    AUTH_MECH = 'SCRAM-SHA-256'

    docdb_secret_var = read_secrets_manager(DOCDB_SECRET_NAME, REGION_NAME)

    MONGODB_HOST = docdb_secret_var['docdbHost']
    MONGODB_PORT = int(docdb_secret_var['docdbPort'])
    MONGODB_AUTHDB = docdb_secret_var['docdbName']
    MONGODB_USER = docdb_secret_var['docdbUserName']
    MONGODB_PWD = docdb_secret_var['docdbPassword']
    MONGO_DB_NAME = docdb_secret_var['docdbName']
    SSL = True
    CA_CERT_FILE = 'rds-combined-ca-bundle.pem'
else:
    # DB Details
    MONGODB_HOST = "localhost"
    MONGODB_PORT = 27017
    MONGO_DB_NAME = "parsed_data"
    MONGODB_AUTHDB = None

# Error msg Strings
ERROR_MSG_METHOD_NOT_ALLOWED = "The resource doesn't support the specified HTTP verb."
ERROR_MSG_JSON_INVALID = "Failed to decode JSON object"
ERROR_MSG_MATCHING_TYPE_INVALID = "Please provide valid matching type string."
ERROR_MSG_JOB_INVALID = "Please provide valid job object"
ERROR_MSG_RESUME_INVALID = "Please provide valid resume object"
ERROR_MSG_SERVER_ERROR = "Servers are not working as expected. The request is probably valid but needs to be requested again later."
ERROR_MSG_INVALID_TOKEN = "Could not validate credentials"
ERROR_MSG_UNAME_AND_PASS_NOT_MATHCED = "Incorrect username or password"

# DB Fields
NORM_JOB_TYPE_FIELD = "jobTypeNormData"
NORM_INDUSTRY_FIELD = "industryNormData"
OVERALL_NORM_INDUSTRY_FIELD = "overallIndustryNormData"
NORM_EDUCATION_FIELD = "educationNormData"
NORM_LOCATION_FIELD = "locationNormData"
NORM_EXPERIENCE_FIELD = "experienceNormData"
NORM_SKILLS_FIELD = "skillsNormData"
NORM_TITLE_FIELD = "titleNormData"
NORMALIZED_SKILLS_FIELD = "NormalizedDomainSkills"
NORMALIZED_COMMON_SKILLS_FIELD = "NormalizedCommonSkills"
NORMALIZED_MUST_HAVE_SKILLS_FIELD = "NormalizedMustHaveSkills"
MUST_HAVE_SKILLS_FIELD = "MustHaveSkills"
OVERALL_EXPERIENCE_FIELD = "OverallExperience"
SKILL_WISE_EXPERIENCE_FIELD = "SkillExperience"
SKILL_EXP_NAME_FIELD = "skill"
SKILL_EXP_COUNT_FIELD = "experience"
SKILL_EXP_LAST_USED_FIELD = "lastUsed"
PARSED_DATA_FIELD = "parsed_data"
NORM_CERT_FIELD = "Certifications"

# Jobs collection fields
JOB_TITLE_FIELD_IN_JOBS = "job_title"
MAJOR_FIELD_IN_JOBS = "major"
DEGREE_FIELD_IN_JOBS = "degree"
COURSE_FIELD_IN_JOBS = "course"
CITY_FIELD_IN_JOBS = "city"
STATE_FIELD_IN_JOBS = "state"
COUNTRY_FIELD_IN_JOBS = "country"
LOCATION_FIELD_IN_JOBS = "location"
JOB_TYPE_FIELD_IN_JOBS = "job_type"
JOB_DESCRIPTION_FIELD_IN_JOBS = "job_description"
JOB_CATEGORY_FIELD_IN_JOBS = "category"
JOB_EXPERIENCE_FIELD_IN_JOBS = "experience"
HIRE_TYPE_FIELD_IN_JOBS = "hire_type"
SKILLS_FIELD_IN_JOBS = "skills"
PARSED_EDUCATION_FIELD = "Education"
PARSED_EXPERIENCE_FIELD = "Experience"
PARSED_OVERALL_EXPERIENCE_FIELD = "OverallExperience"
PARSED_SKILL_EXPERIENCE_FIELD = "SkillExperience"
PARSED_SKILL_EXP_COUNT_FIELD = "Experience"
PARSED_SKILL_EXP_NAME_FIELD = "Experience In"
PARSED_INDUSTRY_FIELD = "Industry"
PARSED_SOC_FIELD = "socCode"
PARSED_TITLES_FIELD = "JobTitles"
PARSED_MAIN_JOB_TITLE_FIELD = "NormalizedMainJobTitle"

# Resume collection fields
JOB_TITLE_FIELD_IN_RESUMES = "role"
RESUME_TITLE_FIELD_IN_RESUMES = "role"
MAJOR_FIELD_IN_RESUMES = "major"
DEGREE_FIELD_IN_RESUMES = "degree"
COURSE_FIELD_IN_RESUMES = "course"
SCHOOL_NAME_FIELD_IN_RESUMES = "school"
UNIVERSITY_FIELD_IN_RESUMES = "university"
SCHOOL_TYPE_FIELD_IN_RESUMES = "school_type"
CITY_FIELD_IN_RESUMES = "city"
STATE_FIELD_IN_RESUMES = "state"
COUNTRY_FIELD_IN_RESUMES = "country"
LOCATION_FIELD_IN_RESUMES = "location"
JOB_TYPE_FIELD_IN_RESUMES = "job_type"
JOB_DESCRIPTION_FIELD_IN_RESUMES = "job_description"

# Location Normalization API Details
# LOCATION_API_URL = "https://dev-location.simplifyapis.com/v1/location/normalizeLocation"
LOCATION_API_URL = "https://api-dev-resume-normalization.zepptalentz.com/v1/location/normalizeLocation"
LOCATION_API_LOCATION_FIELD = "location"
LOCATION_API_RESPONSE_FIELD = "data"
LOCATION_API_ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzaW1wYWktZHMiLCJleHAiOjE2NDEzNzkyNDN9.MLWA9gEqPPKT-O4X9uYfz6QKWdaR9aqSYDQMoXOrQXo"

# Job Type/Level Classifier API
# JOB_TYPE_API_URL = "https://job-level-clf.simplifyapis.com/classify/"
JOB_TYPE_API_URL = "https://api-dev-job-level-classification.zepptalentz.com/classify/"
JOB_TYPE_API_TITLE_FIELD = "jobTitle"
JOB_TYPE_API_EXPERIENCES_FIELD = "experienceTexts"
JOB_TYPE_API_SOC_FIELD = "socCode"
JOB_TYPE_API_JOB_TYPE_FIELD = "jobType"
JOB_TYPE_API_RESPONSE_JOB_TYPE_FIELD = "jobTypes"
JOB_TYPE_API_RESPONSE_JOB_LEVEL_FIELD = "jobLevel"
JOB_TYPE_API_RESPONSE_JOB_ROLE_FIELD = "jobRole"
JOB_TYPE_API_RESPONSE_JOB_NATURE_FIELD = "jobNature"
JOB_TYPE_API_RESPONSE_WORK_HOURS_FIELD = "workHours"
JOB_TYPE_API_RESPONSE_WORK_LOCATION_FIELD = "workLocation"
JOB_TYPE_API_RESPONSE_EXPERIENCE_COUNT_FIELD = "experienceCount"
JOB_TYPE_API_ACCESS_TOKEN =  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzaW1wYWktam9iLWxldmVsLWNsZiIsImV4cCI6NjE2NDU1MTk0NDN9.etsxGXt9xTQBoUq0L7uOXpwdjZpNMh77yx-219faoH0"
# Management Level Fields
MANAGEMENT_LEVEL_FIELD = "managementLevel"
MANAGEMENT_LEVEL_FROM_JOB_ROLES = {"Lead", "Manager", "Executive"}
LOW_MANAGEMENT_LEVEL_VALUE = "low"
MID_MANAGEMENT_LEVEL_VALUE = "mid"
HIGH_MANAGEMENT_LEVEL_VALUE = "high"
EXPERIENCE_WISE_MANAGEMENT_LEVELS = {
    (0, 3): LOW_MANAGEMENT_LEVEL_VALUE,
    (3, 10): MID_MANAGEMENT_LEVEL_VALUE,
    (10, float('inf')): HIGH_MANAGEMENT_LEVEL_VALUE
}

# Title Normalization API
# TITLE_NORM_API_URL = "https://title-normalizer.simplifyapis.com/normalize/"
TITLE_NORM_API_URL = "https://api-dev-skill-taxonomy.zepptalentz.com/normalize/"
TITLE_NORM_API_JOBS_FIELD = "jobs"
TITLE_NORM_API_TITLE_FIELD = "title"
TITLE_NORM_API_RESPONSE_FIELD = "normalized_jobs"
TITLE_NORM_API_RESPONSE_NORM_TITLE_FIELD = "normalized title"
TITLE_NORM_API_RESPONSE_SCORE_FIELD = "similarity score"
TITLE_NORM_API_ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzaW1wYWktZHMiLCJleHAiOjU0MjgwMTgwMzl9.WE_f5hyPLBX2eV-unm9ARy0JG2OfKSv3Cf8tu9yNvhc"

# Education Normalization API
# EDUCATION_NORM_API_URL = "https://education-normalization.simplifyapis.com/normalize/"
EDUCATION_NORM_API_URL = "https://api-dev-education-normalizer.zepptalentz.com/normalize/"
EDUCATION_NORM_API_MAJOR_FIELD = "major"
EDUCATION_NORM_API_DEGREE_FIELD = "degree"
EDUCATION_NORM_API_COURSE_FIELD = "course"
EDUCATION_NORM_API_SCHOOL_FIELD = "school"
EDUCATION_NORM_API_UNIVERSITY_FIELD = "university"
EDUCATION_NORM_API_CITY_FIELD = "city"
EDUCATION_NORM_API_STATE_FIELD = "state"
EDUCATION_NORM_API_COUNTRY_FIELD = "country"
EDUCATION_NORM_API_LOCATION_FIELD = "location"
EDUCATION_NORM_API_SCHOOL_TYPE_FIELD = "schoolType"
EDUCATION_NORM_API_EDUCATION_FIELD = "educations"
EDUCATION_NORM_API_RESPONSE_NORMALIZED_EDUCATIONS_FIELD = "normalizedEducations"
EDUCATION_NORM_API_ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzaW1wYWktZHMiLCJleHAiOjYxNjQ1NTI3MzM3fQ.IPjuwXhYKDoEMcLOHf7ij4sW4iRjRgyKMMa7vQCck5E"

# Industry classifier API
# INDUSTRY_CLF_API_URL = "https://classifier-api.simplifyapis.com"
INDUSTRY_CLF_API_URL = "https://api-dev-industry-classifier.zepptalentz.com"
INDUSTRY_CLF_API_CLF_CONTEXT = "/classify/"
INDUSTRY_CLF_API_CATEGORIZATION_CONTEXT = "/categorize_skills/"
INDUSTRY_CLF_API_REQUEST_JOBS_FIELD = "jobs"
INDUSTRY_CLF_API_JOB_TITLE_FIELD = "mainJobTitle"
INDUSTRY_CLF_API_SKILLS_FIELD = "skills"
INDUSTRY_CLF_API_COMMON_SKILLS_FIELD = "commonSkills"
INDUSTRY_CLF_API_RESPONSE_INDUSTRIES_FIELD = "industries"
INDUSTRY_CLF_API_CONFIDENCE_FIELD = "predictionConfidence"
INDUSTRY_CLF_API_RESPONSE_SOC_FIELD = "socCode"
INDUSTRY_CLF_API_INDUSTRY_WISE_SKILLS_FIELD = "industryWiseSkills"
INDUSTRY_CLF_API_ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzaW1wYWktaW5kdXN0cnktY2xmIiwiZXhwIjo1NDI4MDI4Nzc2fQ.Ujzf84KCJkogzsRsgxMgHVXwvQSya394-VvUNOO9SJc"

# Skills Normalization API
SKILLS_NORM_API_URL = "/normalize_skills"
SKILLS_NORM_API_REQUEST_SKILLS_FIELD = "Skills"
SKILLS_NORM_API_RESPONSE_SKILLS_FIELD = "clean_skills"
#RESUME_SKILLS_NORM_API_URL1 = "https://dev-parser.simplify-ai.com/job_parser/normalize_skills"
#RESUME_SKILLS_NORM_API_URL = "https://dev-job-parser.simplifyapis.com/api/v1/normalize_skills"
# RESUME_SKILLS_NORM_API_URL = "https://skills-normalization.simplifyapis.com/api/skill_normalization"
RESUME_SKILLS_NORM_API_URL = "https://api-dev-skill-normalization.zepptalentz.com/api/skill_normalization"
RESUME_NORMALIZATION_MAIN_KEY = "resume"

# Miscellaneous
RECENCY_RANGE_FOR_WORKX_PRIORITY = {
    (0, 1): 1.0,
    (1, 3): 0.8,
    (3, 5): 0.67,
    (5, 7): 0.5,
    (7, float('inf')): 0.1
}
