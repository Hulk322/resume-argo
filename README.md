
----------------------------------------------------------------------------------------------------
										Resume Normalization API
----------------------------------------------------------------------------------------------

## Steps to build and run with docker: 

**Step 1:** Build docker image
`sudo docker build -t resume_norm_api .`


**Step 2:** Run docker image 
`sudo docker run -it -p 9028:9028 resume_norm_api`


## Steps to Launch: 

**Step 1:** Install the required softwares.

```nodejs
1. Python 3.6.9
```


**Step 2:** Upgrade pip
 
```nodejs
python3 -m pip install --upgrade pip setuptools
```

**Step 3:** Clone Scripts
 
```nodejs
git clone https://ankitsingh8@bitbucket.org/simplifyai/resume_normalization_api.git
```

**Step 4:** Move into Repo Directory
 
```nodejs
cd resume_normalization_api/
```

**Step 5:** Install Required libraries (pymongo and python-decouple are additional library used for creating endpoint for job board)
 
```nodejs
pip3 install -r requirements.txt
```


**Step 6:** Change config parameters to point to appropriate DB

```nodejs
vi config.py
```

**Step 7:** Start API (change start file to main.py as suggested by Devops team):
 
```nodejs
python3 -u main.py
```

## Sample Request

**Request Type:** [POST]

**URL:** http://localhost:9028/resume/normalization

**Request:**

```json
{
  "parse_response": {
    "file_name": "file_Uvs4FLcnonhUHzwsqgw6dT.pdf",
    "parse_time_sec": 4,
    "parsed_resume": {
        "parser_version": "1.3.0",
        "cv_type": "single_sided",
        "text_mode": "pymudf",
        "data": {
            "file_name": "file_Uvs4FLcnonhUHzwsqgw6dT.json",
            "total_experience (in months)": 107,
            "raw_text": "Shweta Mishra\n07845278930 | 07424771922 | 02037230579 | shwetamishra8586@gmail.com | Immediately Available | Long-term Dependent Permit | Hounslow - TW31NB | LinkedIn  \nAnalytics professional with 10 years of experience in complex data analytics across varied domains including Retail, FMCG, Music, Media and \nMovies with solid experience in establishing and turning around analytics practices by creating winning teams \nSKILLSET \nManagement: Project Management (7. 5 years) ★★★★★, Client Management (9 years) ★★★★★, People / Line Management (8 years) ★★★★★, \nVendor Management (3.5 years) ★★★★★, Account Management (3.5 years) ★★★, Agile Management (2.5 years) ★★★ \nVisualization: Excel VBA Dashboards (9 years) ★★★★★, Tableau Dashboards (2 years) ★★★, Power BI Dashboards (2 years) ★★★ \nData Handling & Query Languages: VB Scripting (9 years) ★★★★★, SQL (3 years) ★★★, Python (1.5 years) ★★, R (1 year) ★★, SPSS (2 years) ★★★, \nHive (1 year) ★★, SAP Hana (1 year) ★★, Hadoop (1 year) ★★ \nTools: MS Office (9 years) ★★★★, Google Analytics (1 year) ★★★, Adobe Omniture (2 years) ★★, Qlikview Reports (1 year) ★★, Alteryx (1 year) ★★ \nInformation Tracking: Jira/Yodiz (3.5 years) ★★★★★, Confluence (2 years) ★★★★★, Slack/Trello (1.5 years) ★★★★★, GitHub (1.5 years) ★★★ \nWORK EXPERIENCE \nTredence Inc. , Bangalore, India \nOver a span of 1.25 years, built analytical roadmaps and strategy while managing multiple data science delivery teams and liaising internal and \nexternal stakeholders \nAnalytics Manager: April 2018 – June 2019 (1 year, 3 months) \nRetail Analytics in US Market for ‘Walmart’ \n Mentored and augmented multiple Store, Omni and Digital Marketing teams with 35 data scientists working on real time big data \nleveraging SQL, Python, Tableau, Power BI, Omniture, Alteryx while liaising resources across divisions for creating holistic solutions \n Setup and drove governance by establishing processes, practices, MBR & QBRs, learning goals and robust automations \n Led successful delivery of prediction models using regression, boosted models and target clusters using k-means, KNN, fuzzy c-means \n Drove customer acquisition strategies, marketing effectiveness, campaign success management, business profitability, and actionable \nconsumer insights  \nFMCG Analytics in US Market for ‘Kimberly Clark’ \n Successfully converted and implemented project ideas on trade promotion effectiveness, financial forecasting, personalized \nrecommendation engines, chatbots, and price erosion identification among others \n Spearheaded performance initiatives including redesigning several existing Tableau dashboards to improve response time, building new \ndata strategies, creating data lakes to integrate multiple data sources \nKey Achievement: Established winning teams that led to three folds growth within 3 months and led new engagements from inception \ntaking them to half a million dollar account within a quarter and created a potential of over 3 million \n Applied Skills: SAP HANA, Hive, Hadoop, Python, Jupyter, GitHub, PowerBI, Tableau, VBA, Omniture, Dataroma, Alteryx, Jira, Confluence \n Role: Team handling of up to 35 members with 3 hierarchy level, Client Management, Stakeholder Management, Hiring and Resourcing, \nP&L/Budget \nWNS Analytics , Bangalore, India \nOver a span of 8 years, held multiple positions and worked with numerous major brands building product based solutions like Brandttitude  and \nSocioSEER , creating several optimizations and forecasting models, clustering and profiling their audience, analysing reality television shows, \ndriving shopper insights team, defining their consumer behavioural landscape, beverage occasions and brand equity \nGroup Manager: October 2016 – April 2018 (1 year, 7 months) \nInventory Analytics in US Market for ‘NBC Universal’  \n Led a team of data scientist and statisticians for demand forecasting, inventory allocations, opportunity sizing and refining KPIs and \nbenchmarks for the movie releases at retail store outlets \n Designed national goal setting model for new movie releases using mixed non-linear regression models further used as a base for physical \nand digital forecasting at retailer level for all the future releases \n Increased overall allocation accuracy by 25% and process efficiencies by 70% by constantly improvising the existing models through error \ntracking, retraining models, and automation \n Successful implementation of allocation designs across retail space resulted in multi million savings every quarter by optimized production  \nKey Achievement: ‘Trendsetter Award’ for exceptional stakeholder management  \nApplied Skills: R, Advance Excel, VBA, PowerBI, PowerPoint  \nRole: Team handling of 8 members with 3 hierarchy levels, Client and Stakeholder Management, Hiring and Resourcing \nDeputy Manager: October 2013 – September 2016 (3 years) \nAudience Measurement & Profiling and Pricing Analytics in UK, US & International Market for ‘Sony Music and Entertainment’ \n Created pricing strategy by defining product lifecycle by genre of music albums digital and physical sales by using multivariate regression \nShweta Mishra   |   Page 1 of 2 \n Spearheaded the creation and management of a web-based Audience Profiling Dashboard leveraging Google Analytics and its usability and \nintuitive design led to its extension from a pilot of 5 countries to over 40 countries with yearly refreshes \n Successfully analysed weekly progress of a live reality music television show analysing social media sentiment around all the contestants \n Managed the end to end projects, client relationship, service delivery throughout the territory from inception to execution and impact \nincluding financial and legal aspects like contracting, invoicing, vendor documents, vendor and team NDAs  \nKey Achievement: Received ‘Achiever Award’ for driving efficiencies while multi-tasking, ‘Silver Globe Award’ for years of commitment \nand dedication and ‘Standing Ovation Award’ for thought leadership, consistent ideation, high involvement and initiative \nApplied Skills: MySQL, D3 Library, GitHub, Advance Excel, VBA, PowerPoint, Yodiz, Google Analytics \nRole: Team handling of 5 to 6 members with 2 hierarchy levels, Client, Vendor and Stakeholder Management, Hiring  \nAssistant Manager: April 2012 – September 2013 (1 year, 6 months) \nFMCG, Brand & Consumer Behaviour Analysis in US and International Market for ‘The Coca-Cola Company’ \n Facilitated new brand launch of a mid-calorie beverage in the US markets by analysing product penetration by measuring trial, repeats, \nbasket, source, promotion effectiveness and consumer profile \n Solved various business problems using Gap Analysis, Segmentation-Targeting-Positioning, Market Basket Analysis, Affinity studies, and \nSocial Media and sentiment analysis (leveraging Synthesio and Sysomos) \n Automated entire reporting deliverables and generated advanced analytics roles while heading the Business Planning offshore team \nKey Achievement: Received 'Star Fire' Award for continuous operational excellence \nApplied Skills: SPSS, Advance Excel, VBA, Tableau, PowerPoint, Nielsen AOD, Synthesio, Sysomos \nRole: Team handling of 2-3 members and client management, Hiring \nSenior Business Analyst: April 2011 – March 2012 (1 year) \nShopper Insights in US Market for ‘The Coca-Cola Company’ \n Drove Shopper insights and Dining In analysis across multiple channels like Retail, Food Services, On-Premise, QSR, Fine Dining to analyse \nconsumer profiling, behavioural analysis, path-to-purchase  and developed various dashboards, scorecards and automation tools \n Built algorithms for customer segmentation and profiling for identifying behavioural patterns using the demographic and lifestyle metrics  \n Generated insights around consumer affinity, perception measurement, immediate/future consumption patterns, impulsive buyer \nstrategy, hydration portfolio, retailer associations while leveraging various techniques like A/B testing, correlation, regression and t-test  \nKey Achievement: Awarded 'Shooting Star' for successfully handling critical deliveries and maintaining consistent deliverable quality  \nApplied Skills: SPSS, Advance Excel, VBA, PowerPoint, Nielsen CASE \nRole: Individual contributor and client management \nBusiness Analyst: March 2010 – March 2011 (1 year, 1 month) \nBrand & Consumer Behaviour Analysis in US and International Market for ‘The Coca-Cola Company’ \n Undertook automation for reports and on-going projects and drove 30-90% efficiencies with timely delivery and high quality and smooth \neveryday operation \n Managed direct interactions with client’s senior management for understanding the business requirements and debriefing the team  \nKey Achievement: Awarded 'Shining Star' for being the fastest learner of both business and technology  \nApplied Skills: MS Access, MS Excel, VBA, PowerPoint, Canadian, Euromonitor \nRole: Team player and client interactions \nStandard Chartered , Bangalore, India \nEDUCATION \nPost Graduate in Business Management1 | M.S. Ramaiah Institute of Management, Bangalore, India (2007-2009) \nSpecialization: Marketing | Other Relevant Modules: Statistics, Mathematics, and Economics \nBachelor of Commerce | University of Lucknow, India (2004-2007) \nKey Modules: Statistics, Economics, Finance, Marketing, Sales, Accounting, Law \n1 2 years full time, MBA Equivalent course, with Dual Specialization in Marketing and HR \nShweta Mishra   |   Page 2 of 2 ",
            "personal details": {
                "candidate_name": "Shweta Mishra",
                "email": "shwetamishra8586@gmail.com",
                "contact_no": []
            },
            "experience_segment": true,
            "experience": [
                {
                    "sequence": 1,
                    "organization": [
                        "RETAIL ANALYTICS",
                        "WALMART"
                    ],
                    "role": [
                        "Analytics Manager"
                    ],
                    "from": "04/2018",
                    "to": "06/2019",
                    "skills": [
                        {
                            "skills_name": "analytics",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "retail",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "mentored",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "digital marketing",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "teams",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "big data",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "sql",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "python",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "tableau",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "power bi",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "omniture",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "alteryx",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "governance",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "delivery",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "prediction",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "regression",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "c",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "customer acquisition strategies",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "consumer insights",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "fmcg",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "trade",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "financial forecasting",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "price",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "erosion",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "redesigning",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "data strategies",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "data lakes",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "account",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "sap",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "hana",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "hive",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "jupyter",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "github",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "vba",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "jira",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "confluence",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "client management",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "stakeholder management",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "hiring",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "resourcing",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "budget",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "optimizations",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "forecasting models",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "clustering",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "shopper insights",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        },
                        {
                            "skills_name": "brand equity",
                            "totalMonths": 14,
                            "LastUsed": "06/2019"
                        }
                    ],
                    "description": " Analytics Manager: April 2018 – June 2019 (1 year, 3 months)   Retail Analytics in US Market for ‘Walmart’    Mentored and augmented multiple Store, Omni and Digital Marketing teams with 35 data scientists working on real time big data   leveraging SQL, Python, Tableau, Power BI, Omniture, Alteryx while liaising resources across divisions for creating holistic solutions    Setup and drove governance by establishing processes, practices, MBR & QBRs, learning goals and robust automations    Led successful delivery of prediction models using regression, boosted models and target clusters using k-means, KNN, fuzzy c-means    Drove customer acquisition strategies, marketing effectiveness, campaign success management, business profitability, and actionable   consumer insights   FMCG Analytics in US Market for ‘Kimberly Clark’    Successfully converted and implemented project ideas on trade promotion effectiveness, financial forecasting, personalized   recommendation engines, chatbots, and price erosion identification among others    Spearheaded performance initiatives including redesigning several existing Tableau dashboards to improve response time, building new   data strategies, creating data lakes to integrate multiple data sources   Key Achievement: Established winning teams that led to three folds growth within 3 months and led new engagements from inception   taking them to half a million dollar account within a quarter and created a potential of over 3 million   Applied Skills: SAP HANA, Hive, Hadoop, Python, Jupyter, GitHub, PowerBI, Tableau, VBA, Omniture, Dataroma, Alteryx, Jira, Confluence   Role: Team handling of up to 35 members with 3 hierarchy level, Client Management, Stakeholder Management, Hiring and Resourcing,   P&L/Budget   WNS Analytics , Bangalore, India   Over a span of 8 years, held multiple positions and worked with numerous major brands building product based solutions like Brandttitude  and   SocioSEER , creating several optimizations and forecasting models, clustering and profiling their audience, analysing reality television shows,   driving shopper insights team, defining their consumer behavioural landscape, beverage occasions and brand equity "
                },
                {
                    "sequence": 2,
                    "organization": [
                        "NBC UNIVERSAL"
                    ],
                    "role": [
                        "Group Manager"
                    ],
                    "titles": [
                        "Data Scientist"
                    ],
                    "from": "10/2016",
                    "to": "04/2018",
                    "skills": [
                        {
                            "skills_name": "inventory",
                            "totalMonths": 18,
                            "LastUsed": "04/2018"
                        },
                        {
                            "skills_name": "analytics",
                            "totalMonths": 18,
                            "LastUsed": "04/2018"
                        },
                        {
                            "skills_name": "demand forecasting",
                            "totalMonths": 18,
                            "LastUsed": "04/2018"
                        },
                        {
                            "skills_name": "allocations",
                            "totalMonths": 18,
                            "LastUsed": "04/2018"
                        },
                        {
                            "skills_name": "sizing",
                            "totalMonths": 18,
                            "LastUsed": "04/2018"
                        },
                        {
                            "skills_name": "retail",
                            "totalMonths": 18,
                            "LastUsed": "04/2018"
                        },
                        {
                            "skills_name": "outlets",
                            "totalMonths": 18,
                            "LastUsed": "04/2018"
                        },
                        {
                            "skills_name": "linear regression",
                            "totalMonths": 18,
                            "LastUsed": "04/2018"
                        },
                        {
                            "skills_name": "regression models",
                            "totalMonths": 18,
                            "LastUsed": "04/2018"
                        },
                        {
                            "skills_name": "forecasting",
                            "totalMonths": 18,
                            "LastUsed": "04/2018"
                        },
                        {
                            "skills_name": "allocation",
                            "totalMonths": 18,
                            "LastUsed": "04/2018"
                        },
                        {
                            "skills_name": "automation",
                            "totalMonths": 18,
                            "LastUsed": "04/2018"
                        },
                        {
                            "skills_name": "designs",
                            "totalMonths": 18,
                            "LastUsed": "04/2018"
                        },
                        {
                            "skills_name": "stakeholder management",
                            "totalMonths": 18,
                            "LastUsed": "04/2018"
                        },
                        {
                            "skills_name": "r",
                            "totalMonths": 18,
                            "LastUsed": "04/2018"
                        },
                        {
                            "skills_name": "advance excel",
                            "totalMonths": 18,
                            "LastUsed": "04/2018"
                        },
                        {
                            "skills_name": "vba",
                            "totalMonths": 18,
                            "LastUsed": "04/2018"
                        },
                        {
                            "skills_name": "hiring",
                            "totalMonths": 18,
                            "LastUsed": "04/2018"
                        },
                        {
                            "skills_name": "resourcing",
                            "totalMonths": 18,
                            "LastUsed": "04/2018"
                        }
                    ],
                    "description": " Group Manager: October 2016 – April 2018 (1 year, 7 months)   Inventory Analytics in US Market for ‘NBC Universal’    Led a team of data scientist and statisticians for demand forecasting, inventory allocations, opportunity sizing and refining KPIs and   benchmarks for the movie releases at retail store outlets    Designed national goal setting model for new movie releases using mixed non-linear regression models further used as a base for physical   and digital forecasting at retailer level for all the future releases    Increased overall allocation accuracy by 25% and process efficiencies by 70% by constantly improvising the existing models through error   tracking, retraining models, and automation    Successful implementation of allocation designs across retail space resulted in multi million savings every quarter by optimized production   Key Achievement: ‘Trendsetter Award’ for exceptional stakeholder management   Applied Skills: R, Advance Excel, VBA, PowerBI, PowerPoint   Role: Team handling of 8 members with 3 hierarchy levels, Client and Stakeholder Management, Hiring and Resourcing "
                },
                {
                    "sequence": 3,
                    "organization": [
                        "SONY"
                    ],
                    "role": [
                        "Deputy Manager"
                    ],
                    "from": "10/2013",
                    "to": "09/2016",
                    "skills": [
                        {
                            "skills_name": "audience measurement",
                            "totalMonths": 35,
                            "LastUsed": "09/2016"
                        },
                        {
                            "skills_name": "analytics",
                            "totalMonths": 35,
                            "LastUsed": "09/2016"
                        },
                        {
                            "skills_name": "pricing strategy",
                            "totalMonths": 35,
                            "LastUsed": "09/2016"
                        },
                        {
                            "skills_name": "sales",
                            "totalMonths": 35,
                            "LastUsed": "09/2016"
                        },
                        {
                            "skills_name": "regression",
                            "totalMonths": 35,
                            "LastUsed": "09/2016"
                        },
                        {
                            "skills_name": "web",
                            "totalMonths": 35,
                            "LastUsed": "09/2016"
                        },
                        {
                            "skills_name": "google analytics",
                            "totalMonths": 35,
                            "LastUsed": "09/2016"
                        },
                        {
                            "skills_name": "delivery",
                            "totalMonths": 35,
                            "LastUsed": "09/2016"
                        },
                        {
                            "skills_name": "financial",
                            "totalMonths": 35,
                            "LastUsed": "09/2016"
                        },
                        {
                            "skills_name": "legal aspects",
                            "totalMonths": 35,
                            "LastUsed": "09/2016"
                        },
                        {
                            "skills_name": "mysql",
                            "totalMonths": 35,
                            "LastUsed": "09/2016"
                        },
                        {
                            "skills_name": "d3",
                            "totalMonths": 35,
                            "LastUsed": "09/2016"
                        },
                        {
                            "skills_name": "github",
                            "totalMonths": 35,
                            "LastUsed": "09/2016"
                        },
                        {
                            "skills_name": "advance excel",
                            "totalMonths": 35,
                            "LastUsed": "09/2016"
                        },
                        {
                            "skills_name": "vba",
                            "totalMonths": 35,
                            "LastUsed": "09/2016"
                        },
                        {
                            "skills_name": "stakeholder management",
                            "totalMonths": 35,
                            "LastUsed": "09/2016"
                        },
                        {
                            "skills_name": "hiring",
                            "totalMonths": 35,
                            "LastUsed": "09/2016"
                        }
                    ],
                    "description": " Deputy Manager: October 2013 – September 2016 (3 years)   Audience Measurement & Profiling and Pricing Analytics in UK, US & International Market for ‘Sony Music and Entertainment’    Created pricing strategy by defining product lifecycle by genre of music albums digital and physical sales by using multivariate regression   Shweta Mishra   |   Page 1 of 2    Spearheaded the creation and management of a web-based Audience Profiling Dashboard leveraging Google Analytics and its usability and   intuitive design led to its extension from a pilot of 5 countries to over 40 countries with yearly refreshes    Successfully analysed weekly progress of a live reality music television show analysing social media sentiment around all the contestants    Managed the end to end projects, client relationship, service delivery throughout the territory from inception to execution and impact   including financial and legal aspects like contracting, invoicing, vendor documents, vendor and team NDAs   Key Achievement: Received ‘Achiever Award’ for driving efficiencies while multi-tasking, ‘Silver Globe Award’ for years of commitment   and dedication and ‘Standing Ovation Award’ for thought leadership, consistent ideation, high involvement and initiative   Applied Skills: MySQL, D3 Library, GitHub, Advance Excel, VBA, PowerPoint, Yodiz, Google Analytics   Role: Team handling of 5 to 6 members with 2 hierarchy levels, Client, Vendor and Stakeholder Management, Hiring "
                },
                {
                    "sequence": 4,
                    "organization": [
                        "THE COCA - COLA COMPANY"
                    ],
                    "role": [
                        "Assistant Manager"
                    ],
                    "from": "04/2012",
                    "to": "09/2013",
                    "skills": [
                        {
                            "skills_name": "fmcg",
                            "totalMonths": 17,
                            "LastUsed": "09/2013"
                        },
                        {
                            "skills_name": "coca cola",
                            "totalMonths": 17,
                            "LastUsed": "09/2013"
                        },
                        {
                            "skills_name": "product penetration",
                            "totalMonths": 17,
                            "LastUsed": "09/2013"
                        },
                        {
                            "skills_name": "gap analysis",
                            "totalMonths": 17,
                            "LastUsed": "09/2013"
                        },
                        {
                            "skills_name": "segmentation",
                            "totalMonths": 17,
                            "LastUsed": "09/2013"
                        },
                        {
                            "skills_name": "targeting",
                            "totalMonths": 17,
                            "LastUsed": "09/2013"
                        },
                        {
                            "skills_name": "positioning",
                            "totalMonths": 17,
                            "LastUsed": "09/2013"
                        },
                        {
                            "skills_name": "market basket analysis",
                            "totalMonths": 17,
                            "LastUsed": "09/2013"
                        },
                        {
                            "skills_name": "sentiment analysis",
                            "totalMonths": 17,
                            "LastUsed": "09/2013"
                        },
                        {
                            "skills_name": "sysomos",
                            "totalMonths": 17,
                            "LastUsed": "09/2013"
                        },
                        {
                            "skills_name": "analytics",
                            "totalMonths": 17,
                            "LastUsed": "09/2013"
                        },
                        {
                            "skills_name": "business planning",
                            "totalMonths": 17,
                            "LastUsed": "09/2013"
                        },
                        {
                            "skills_name": "fire",
                            "totalMonths": 17,
                            "LastUsed": "09/2013"
                        },
                        {
                            "skills_name": "spss",
                            "totalMonths": 17,
                            "LastUsed": "09/2013"
                        },
                        {
                            "skills_name": "advance excel",
                            "totalMonths": 17,
                            "LastUsed": "09/2013"
                        },
                        {
                            "skills_name": "vba",
                            "totalMonths": 17,
                            "LastUsed": "09/2013"
                        },
                        {
                            "skills_name": "tableau",
                            "totalMonths": 17,
                            "LastUsed": "09/2013"
                        },
                        {
                            "skills_name": "nielsen",
                            "totalMonths": 17,
                            "LastUsed": "09/2013"
                        },
                        {
                            "skills_name": "aod",
                            "totalMonths": 17,
                            "LastUsed": "09/2013"
                        },
                        {
                            "skills_name": "client management",
                            "totalMonths": 17,
                            "LastUsed": "09/2013"
                        },
                        {
                            "skills_name": "hiring",
                            "totalMonths": 17,
                            "LastUsed": "09/2013"
                        }
                    ],
                    "description": " Assistant Manager: April 2012 – September 2013 (1 year, 6 months)   FMCG, Brand & Consumer Behaviour Analysis in US and International Market for ‘The Coca-Cola Company’    Facilitated new brand launch of a mid-calorie beverage in the US markets by analysing product penetration by measuring trial, repeats,   basket, source, promotion effectiveness and consumer profile    Solved various business problems using Gap Analysis, Segmentation-Targeting-Positioning, Market Basket Analysis, Affinity studies, and   Social Media and sentiment analysis (leveraging Synthesio and Sysomos)    Automated entire reporting deliverables and generated advanced analytics roles while heading the Business Planning offshore team   Key Achievement: Received 'Star Fire' Award for continuous operational excellence   Applied Skills: SPSS, Advance Excel, VBA, Tableau, PowerPoint, Nielsen AOD, Synthesio, Sysomos   Role: Team handling of 2-3 members and client management, Hiring "
                },
                {
                    "sequence": 5,
                    "organization": [
                        "THE COCA - COLA COMPANY"
                    ],
                    "role": [
                        "Senior Business Analyst"
                    ],
                    "from": "04/2011",
                    "to": "03/2012",
                    "skills": [
                        {
                            "skills_name": "shopper insights",
                            "totalMonths": 11,
                            "LastUsed": "03/2012"
                        },
                        {
                            "skills_name": "coca cola",
                            "totalMonths": 11,
                            "LastUsed": "03/2012"
                        },
                        {
                            "skills_name": "retail",
                            "totalMonths": 11,
                            "LastUsed": "03/2012"
                        },
                        {
                            "skills_name": "qsr",
                            "totalMonths": 11,
                            "LastUsed": "03/2012"
                        },
                        {
                            "skills_name": "fine dining",
                            "totalMonths": 11,
                            "LastUsed": "03/2012"
                        },
                        {
                            "skills_name": "automation tools",
                            "totalMonths": 11,
                            "LastUsed": "03/2012"
                        },
                        {
                            "skills_name": "segmentation",
                            "totalMonths": 11,
                            "LastUsed": "03/2012"
                        },
                        {
                            "skills_name": "lifestyle",
                            "totalMonths": 11,
                            "LastUsed": "03/2012"
                        },
                        {
                            "skills_name": "regression",
                            "totalMonths": 11,
                            "LastUsed": "03/2012"
                        },
                        {
                            "skills_name": "test",
                            "totalMonths": 11,
                            "LastUsed": "03/2012"
                        },
                        {
                            "skills_name": "deliveries",
                            "totalMonths": 11,
                            "LastUsed": "03/2012"
                        },
                        {
                            "skills_name": "spss",
                            "totalMonths": 11,
                            "LastUsed": "03/2012"
                        },
                        {
                            "skills_name": "advance excel",
                            "totalMonths": 11,
                            "LastUsed": "03/2012"
                        },
                        {
                            "skills_name": "vba",
                            "totalMonths": 11,
                            "LastUsed": "03/2012"
                        },
                        {
                            "skills_name": "nielsen",
                            "totalMonths": 11,
                            "LastUsed": "03/2012"
                        },
                        {
                            "skills_name": "client management",
                            "totalMonths": 11,
                            "LastUsed": "03/2012"
                        }
                    ],
                    "description": " Senior Business Analyst: April 2011 – March 2012 (1 year)   Shopper Insights in US Market for ‘The Coca-Cola Company’    Drove Shopper insights and Dining In analysis across multiple channels like Retail, Food Services, On-Premise, QSR, Fine Dining to analyse   consumer profiling, behavioural analysis, path-to-purchase  and developed various dashboards, scorecards and automation tools    Built algorithms for customer segmentation and profiling for identifying behavioural patterns using the demographic and lifestyle metrics    Generated insights around consumer affinity, perception measurement, immediate/future consumption patterns, impulsive buyer   strategy, hydration portfolio, retailer associations while leveraging various techniques like A/B testing, correlation, regression and t-test   Key Achievement: Awarded 'Shooting Star' for successfully handling critical deliveries and maintaining consistent deliverable quality   Applied Skills: SPSS, Advance Excel, VBA, PowerPoint, Nielsen CASE   Role: Individual contributor and client management "
                },
                {
                    "sequence": 6,
                    "organization": [
                        "THE COCA - COLA COMPANY"
                    ],
                    "role": [
                        "Business Analyst"
                    ],
                    "from": "03/2010",
                    "to": "03/2011",
                    "skills": [
                        {
                            "skills_name": "coca cola",
                            "totalMonths": 12,
                            "LastUsed": "03/2011"
                        },
                        {
                            "skills_name": "automation",
                            "totalMonths": 12,
                            "LastUsed": "03/2011"
                        },
                        {
                            "skills_name": "delivery",
                            "totalMonths": 12,
                            "LastUsed": "03/2011"
                        }
                    ],
                    "description": " Business Analyst: March 2010 – March 2011 (1 year, 1 month)   Brand & Consumer Behaviour Analysis in US and International Market for ‘The Coca-Cola Company’    Undertook automation for reports and on-going projects and drove 30-90% efficiencies with timely delivery and high quality and smooth   everyday operation    Managed direct interactions with client’s senior management for understanding the business requirements and debriefing the team   Key Achievement: Awarded 'Shining Star' for being the fastest learner of both business and technology "
                }
            ],
            "education_segment": true,
            "education": [
                {
                    "univ": "Ramaiah Institute of Management",
                    "degree": "Post Graduate",
                    "major": "Business Management"
                },
                {
                    "univ": "University of Lucknow India",
                    "degree": "Bachelor",
                    "major": "Commerce"
                },
                {
                    "univ": "",
                    "degree": "MBA",
                    "major": "Accounting Law"
                }
            ],
            "skills_cumulative_exp": [
                {
                    "skills_name": "account",
                    "totalMonths": 14,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "advance excel",
                    "totalMonths": 81,
                    "LastUsed": "04/2018"
                },
                {
                    "skills_name": "allocation",
                    "totalMonths": 18,
                    "LastUsed": "04/2018"
                },
                {
                    "skills_name": "allocations",
                    "totalMonths": 18,
                    "LastUsed": "04/2018"
                },
                {
                    "skills_name": "alteryx",
                    "totalMonths": 14,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "analytics",
                    "totalMonths": 84,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "aod",
                    "totalMonths": 17,
                    "LastUsed": "09/2013"
                },
                {
                    "skills_name": "audience measurement",
                    "totalMonths": 35,
                    "LastUsed": "09/2016"
                },
                {
                    "skills_name": "automation",
                    "totalMonths": 30,
                    "LastUsed": "04/2018"
                },
                {
                    "skills_name": "automation tools",
                    "totalMonths": 11,
                    "LastUsed": "03/2012"
                },
                {
                    "skills_name": "big data",
                    "totalMonths": 14,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "brand equity",
                    "totalMonths": 14,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "budget",
                    "totalMonths": 14,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "business planning",
                    "totalMonths": 17,
                    "LastUsed": "09/2013"
                },
                {
                    "skills_name": "c",
                    "totalMonths": 14,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "client management",
                    "totalMonths": 42,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "clustering",
                    "totalMonths": 14,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "coca cola",
                    "totalMonths": 40,
                    "LastUsed": "09/2013"
                },
                {
                    "skills_name": "confluence",
                    "totalMonths": 14,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "consumer insights",
                    "totalMonths": 14,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "customer acquisition strategies",
                    "totalMonths": 14,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "d3",
                    "totalMonths": 35,
                    "LastUsed": "09/2016"
                },
                {
                    "skills_name": "data lakes",
                    "totalMonths": 14,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "data strategies",
                    "totalMonths": 14,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "deliveries",
                    "totalMonths": 11,
                    "LastUsed": "03/2012"
                },
                {
                    "skills_name": "delivery",
                    "totalMonths": 61,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "demand forecasting",
                    "totalMonths": 18,
                    "LastUsed": "04/2018"
                },
                {
                    "skills_name": "designs",
                    "totalMonths": 18,
                    "LastUsed": "04/2018"
                },
                {
                    "skills_name": "digital marketing",
                    "totalMonths": 14,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "erosion",
                    "totalMonths": 14,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "financial",
                    "totalMonths": 35,
                    "LastUsed": "09/2016"
                },
                {
                    "skills_name": "financial forecasting",
                    "totalMonths": 14,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "fine dining",
                    "totalMonths": 11,
                    "LastUsed": "03/2012"
                },
                {
                    "skills_name": "fire",
                    "totalMonths": 17,
                    "LastUsed": "09/2013"
                },
                {
                    "skills_name": "fmcg",
                    "totalMonths": 31,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "forecasting",
                    "totalMonths": 18,
                    "LastUsed": "04/2018"
                },
                {
                    "skills_name": "forecasting models",
                    "totalMonths": 14,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "gap analysis",
                    "totalMonths": 17,
                    "LastUsed": "09/2013"
                },
                {
                    "skills_name": "github",
                    "totalMonths": 49,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "google analytics",
                    "totalMonths": 35,
                    "LastUsed": "09/2016"
                },
                {
                    "skills_name": "governance",
                    "totalMonths": 14,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "hana",
                    "totalMonths": 14,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "hiring",
                    "totalMonths": 84,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "hive",
                    "totalMonths": 14,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "inventory",
                    "totalMonths": 18,
                    "LastUsed": "04/2018"
                },
                {
                    "skills_name": "jira",
                    "totalMonths": 14,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "jupyter",
                    "totalMonths": 14,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "legal aspects",
                    "totalMonths": 35,
                    "LastUsed": "09/2016"
                },
                {
                    "skills_name": "lifestyle",
                    "totalMonths": 11,
                    "LastUsed": "03/2012"
                },
                {
                    "skills_name": "linear regression",
                    "totalMonths": 18,
                    "LastUsed": "04/2018"
                },
                {
                    "skills_name": "market basket analysis",
                    "totalMonths": 17,
                    "LastUsed": "09/2013"
                },
                {
                    "skills_name": "mentored",
                    "totalMonths": 14,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "mysql",
                    "totalMonths": 35,
                    "LastUsed": "09/2016"
                },
                {
                    "skills_name": "nielsen",
                    "totalMonths": 28,
                    "LastUsed": "09/2013"
                },
                {
                    "skills_name": "omniture",
                    "totalMonths": 14,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "optimizations",
                    "totalMonths": 14,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "outlets",
                    "totalMonths": 18,
                    "LastUsed": "04/2018"
                },
                {
                    "skills_name": "positioning",
                    "totalMonths": 17,
                    "LastUsed": "09/2013"
                },
                {
                    "skills_name": "power bi",
                    "totalMonths": 14,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "prediction",
                    "totalMonths": 14,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "price",
                    "totalMonths": 14,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "pricing strategy",
                    "totalMonths": 35,
                    "LastUsed": "09/2016"
                },
                {
                    "skills_name": "product penetration",
                    "totalMonths": 17,
                    "LastUsed": "09/2013"
                },
                {
                    "skills_name": "python",
                    "totalMonths": 14,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "qsr",
                    "totalMonths": 11,
                    "LastUsed": "03/2012"
                },
                {
                    "skills_name": "r",
                    "totalMonths": 18,
                    "LastUsed": "04/2018"
                },
                {
                    "skills_name": "redesigning",
                    "totalMonths": 14,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "regression",
                    "totalMonths": 60,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "regression models",
                    "totalMonths": 18,
                    "LastUsed": "04/2018"
                },
                {
                    "skills_name": "resourcing",
                    "totalMonths": 32,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "retail",
                    "totalMonths": 43,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "sales",
                    "totalMonths": 35,
                    "LastUsed": "09/2016"
                },
                {
                    "skills_name": "sap",
                    "totalMonths": 14,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "segmentation",
                    "totalMonths": 28,
                    "LastUsed": "09/2013"
                },
                {
                    "skills_name": "sentiment analysis",
                    "totalMonths": 17,
                    "LastUsed": "09/2013"
                },
                {
                    "skills_name": "shopper insights",
                    "totalMonths": 25,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "sizing",
                    "totalMonths": 18,
                    "LastUsed": "04/2018"
                },
                {
                    "skills_name": "spss",
                    "totalMonths": 28,
                    "LastUsed": "09/2013"
                },
                {
                    "skills_name": "sql",
                    "totalMonths": 14,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "stakeholder management",
                    "totalMonths": 67,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "sysomos",
                    "totalMonths": 17,
                    "LastUsed": "09/2013"
                },
                {
                    "skills_name": "tableau",
                    "totalMonths": 31,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "targeting",
                    "totalMonths": 17,
                    "LastUsed": "09/2013"
                },
                {
                    "skills_name": "teams",
                    "totalMonths": 14,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "test",
                    "totalMonths": 11,
                    "LastUsed": "03/2012"
                },
                {
                    "skills_name": "trade",
                    "totalMonths": 14,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "vba",
                    "totalMonths": 95,
                    "LastUsed": "06/2019"
                },
                {
                    "skills_name": "web",
                    "totalMonths": 35,
                    "LastUsed": "09/2016"
                }
            ],
            "domain_skills": [
                "prediction",
                "price",
                "hive",
                "c",
                "account",
                "inventory",
                "linear regression",
                "mysql",
                "customer acquisition strategies",
                "vendor management",
                "jira",
                "github",
                "test",
                "advance excel",
                "financial forecasting",
                "automation tools",
                "turning",
                "designs",
                "sales",
                "r",
                "mentored",
                "forecasting",
                "data analytics",
                "automation",
                "fire",
                "sentiment analysis",
                "financial",
                "budget",
                "confluence",
                "hiring",
                "shopper insights",
                "regression models",
                "big data",
                "qsr",
                "dependent",
                "lifestyle",
                "analytics",
                "business planning",
                "audience measurement",
                "omniture",
                "forecasting models",
                "deliveries",
                "segmentation",
                "tableau",
                "product penetration",
                "consumer insights",
                "data strategies",
                "gap analysis",
                "sap",
                "clustering",
                "python",
                "positioning",
                "optimizations",
                "client management",
                "agile",
                "brand equity",
                "line management",
                "sql",
                "excel vba",
                "redesigning",
                "retail",
                "fine dining",
                "hana",
                "d3",
                "account management",
                "qlikview",
                "web",
                "ms excel",
                "power bi",
                "market basket analysis",
                "spss",
                "delivery",
                "legal aspects",
                "regression",
                "data lakes",
                "pricing strategy",
                "sizing",
                "targeting",
                "slack",
                "alteryx",
                "allocations",
                "jupyter",
                "vba",
                "visualization",
                "nielsen",
                "fmcg",
                "demand forecasting",
                "trade",
                "coca cola",
                "allocation",
                "erosion",
                "governance",
                "google analytics",
                "stakeholder management",
                "teams",
                "outlets",
                "digital marketing",
                "trello",
                "resourcing",
                "aod",
                "ms access",
                "vb scripting",
                "sysomos"
            ],
            "common_skills": [
                "team player",
                "client interactions"
            ]
        },
        "success": "true",
        "last_update_date": "13/04/2021 16:23:28",
        "json_out_dir": "./data/json_dir",
        "source_dir": "./data/pdf_dir"
    }
}
}
```

**Response:**

```json
{
  "resume": {
    "industryNormData": [
      {
        "majorGroup": "Management Occupations",
        "minorGroup": "Advertising, Marketing, Promotions, Public Relations, and Sales Managers",
        "broadOccupation": "Marketing and Sales Managers",
        "detailedOccupation": "Marketing Managers",
        "predictionConfidence": 0.9755889538812196,
        "socCode": "11-2021.00"
      },
      {
        "majorGroup": "Management Occupations",
        "minorGroup": "Top Executives",
        "broadOccupation": "General and Operations Managers",
        "detailedOccupation": "General and Operations Managers",
        "predictionConfidence": 0.7057306810399908,
        "socCode": "11-1021.00"
      },
      {
        "majorGroup": "Business and Financial Operations Occupations",
        "minorGroup": "Business Operations Specialists",
        "broadOccupation": "Logisticians and Project Management Specialists",
        "detailedOccupation": "Project Management Specialists",
        "predictionConfidence": 0.28191525621103997,
        "socCode": "11-9199.00"
      },
      {
        "majorGroup": "Management Occupations",
        "minorGroup": "Top Executives",
        "broadOccupation": "General and Operations Managers",
        "detailedOccupation": "General and Operations Managers",
        "predictionConfidence": 0.9987956464816719,
        "socCode": "11-1021.00"
      },
      {
        "majorGroup": "Management Occupations",
        "minorGroup": "Top Executives",
        "broadOccupation": "General and Operations Managers",
        "detailedOccupation": "General and Operations Managers",
        "predictionConfidence": 0.6113074045423446,
        "socCode": "11-1021.00"
      },
      {
        "majorGroup": "Management Occupations",
        "minorGroup": "Advertising, Marketing, Promotions, Public Relations, and Sales Managers",
        "broadOccupation": "Marketing and Sales Managers",
        "detailedOccupation": "Marketing Managers",
        "predictionConfidence": 0.2320939220939317,
        "socCode": "11-2021.00"
      },
      {
        "majorGroup": "Computer and Mathematical Occupations",
        "minorGroup": "Mathematical Science Occupations",
        "broadOccupation": "Data Scientists",
        "detailedOccupation": "Business Intelligence Analysts",
        "predictionConfidence": 0.909068985804078,
        "socCode": "15-2051.01"
      },
      {
        "majorGroup": "Business and Financial Operations Occupations",
        "minorGroup": "Business Operations Specialists",
        "broadOccupation": "Management Analysts",
        "detailedOccupation": "Management Analysts",
        "predictionConfidence": 0.7954497705740335,
        "socCode": "13-1111.00"
      },
      {
        "majorGroup": "Computer and Mathematical Occupations",
        "minorGroup": "Mathematical Science Occupations",
        "broadOccupation": "Data Scientists",
        "detailedOccupation": "Business Intelligence Analysts",
        "predictionConfidence": 0.12325219594276562,
        "socCode": "15-2051.01"
      }
    ],
    "jobTypeNormData": [
      {
        "jobLevel": "Intermediate Level",
        "jobRole": "Manager",
        "jobTypes": {
          "jobNature": "Permanent",
          "workHours": "Full-Time",
          "workLocation": "Office Work"
        }
      },
      {
        "jobLevel": "Intermediate Level",
        "jobRole": "Manager",
        "jobTypes": {
          "jobNature": "Permanent",
          "workHours": "Full-Time",
          "workLocation": "Office Work"
        }
      },
      {
        "jobLevel": "Intermediate Level",
        "jobRole": "Manager",
        "jobTypes": {
          "jobNature": "Permanent",
          "workHours": "Full-Time",
          "workLocation": "Office Work"
        }
      },
      {
        "jobLevel": "Intermediate Level",
        "jobRole": "Manager",
        "jobTypes": {
          "jobNature": "Permanent",
          "workHours": "Full-Time",
          "workLocation": "Office Work"
        }
      },
      {
        "jobLevel": "Entry Level",
        "jobRole": "Senior",
        "jobTypes": {
          "jobNature": "Permanent",
          "workHours": "Full-Time",
          "workLocation": "Office Work"
        }
      },
      {
        "jobLevel": "Entry Level",
        "jobRole": "Manager",
        "jobTypes": {
          "jobNature": "Permanent",
          "workHours": "Full-Time",
          "workLocation": "Office Work"
        }
      }
    ],
    "educationNormData": [
      {
        "normalizedMajor": "Business and Marketing Management",
        "majorNormConfidence": 1,
        "majorAbbreviations": [],
        "normalizedDegree": "Masters Degree",
        "degreeNormConfidence": 1,
        "degreeAbbreviations": [],
        "degreeLevel": "Post-Graduation",
        "normalizedCity": null,
        "normalizedState": "Karnataka",
        "normalizedStateCode": "KA",
        "normalizedCountry": "India",
        "normalizedSchool": "M S RAMAIAH INSTITUTE OF MANAGEMENT",
        "normalizedUniversity": "M S RAMAIAH INSTITUTE OF MANAGEMENT",
        "schoolMatchingScore": 0.8712898284313726,
        "schoolsAbbreviations": [
          "MSRIM",
          "MSRIM - Karnataka"
        ],
        "schoolType": "Institute"
      },
      {
        "normalizedMajor": "Commerce",
        "majorNormConfidence": 1,
        "majorAbbreviations": [],
        "normalizedDegree": "Bachelors Degree",
        "degreeNormConfidence": 1,
        "degreeAbbreviations": [
          "Baccalaureate",
          "bachelor",
          "Bachelor’s",
          "Bachelors",
          "Graduation"
        ],
        "degreeLevel": "Graduation",
        "normalizedCity": "Lucknow",
        "normalizedState": "Uttar Pradesh",
        "normalizedStateCode": "UP",
        "normalizedCountry": "India",
        "normalizedSchool": "University of Lucknow",
        "normalizedUniversity": "UNIVERSITY OF Lucknow",
        "schoolMatchingScore": 0.9516666666666667,
        "schoolsAbbreviations": [],
        "schoolType": "University/College"
      },
      {
        "normalizedMajor": "Accounting and Law",
        "majorNormConfidence": 1,
        "majorAbbreviations": [],
        "normalizedDegree": "Masters of Business Administration",
        "degreeNormConfidence": 1,
        "degreeAbbreviations": [],
        "degreeLevel": "Post-Graduation",
        "normalizedCity": null,
        "normalizedState": null,
        "normalizedStateCode": null,
        "normalizedCountry": null,
        "normalizedSchool": "",
        "normalizedUniversity": "",
        "schoolMatchingScore": 0,
        "schoolsAbbreviations": [],
        "schoolType": null
      }
    ],
    "locationNormData": [],
    "skillsNormData": {
      "NormalizedCommonSkills": [
        "Client Interactions",
        "Team Player"
      ],
      "NormalizedSkills": [
        "C",
        "Delivery",
        "Regression Models",
        "Price",
        "Budget",
        "Turning",
        "Allocation",
        "Omniture",
        "Slack",
        "Sales",
        "R",
        "Trade",
        "Visualization",
        "Shopper Insights",
        "Business planning",
        "Confluence",
        "Advance Excel",
        "Web",
        "Targeting",
        "GitHub",
        "Forecasting Models",
        "Lifestyle",
        "Alteryx",
        "Fire",
        "Financial Forecasting",
        "Product Penetration",
        "Designs",
        "Data Strategies",
        "Customer Acquisition Strategies",
        "Jupyter",
        "Test",
        "Tableau",
        "Coca Cola",
        "Allocations",
        "Client management",
        "Automation Tools",
        "Google Analytics",
        "Audience Measurement",
        "D3.js",
        "Optimizations",
        "Pricing Strategy",
        "Hiring",
        "Excel Vba",
        "Legal Aspects",
        "Teams",
        "Aod",
        "Brand Equity",
        "Sysomos",
        "Analytics",
        "Agile",
        "Automation",
        "Resourcing",
        "Mentored",
        "FMCG",
        "Linear Regression",
        "Data Analytics",
        "Stakeholder management",
        "SPSS",
        "Sentiment Analysis",
        "MySQL",
        "Qsr",
        "Inventory",
        "Nielsen",
        "Trello",
        "SQL",
        "Redesigning",
        "Line Management",
        "Retail",
        "Outlets",
        "Data Lakes",
        "Python",
        "QlikView",
        "VB Scripting",
        "SAP",
        "Regression",
        "Governance",
        "Prediction",
        "Dependent",
        "JIRA",
        "VBA",
        "MS Excel",
        "MS Access",
        "Vendor Management",
        "Gap Analysis",
        "Forecasting",
        "Market Basket Analysis",
        "Account",
        "SAP HANA",
        "Financial",
        "Hive",
        "Positioning",
        "Sizing",
        "Demand Forecasting",
        "Clustering",
        "Deliveries",
        "Big Data",
        "Segmentation",
        "Account Management",
        "Power BI",
        "Erosion",
        "Digital marketing",
        "Fine Dining",
        "Consumer Insights"
      ]
    },
    "titleNormData": [
      {
        "original title": "Analytics Manager",
        "normalized title": "Analytics Manager",
        "similarity score": 1,
        "NormalizedMainJobTitle": "Analytics Manager"
      },
      {
        "original title": "Group Manager",
        "normalized title": "Group Manager",
        "similarity score": 1,
        "NormalizedMainJobTitle": "Group Manager"
      },
      {
        "original title": "Deputy Manager",
        "normalized title": "Deputy Manager",
        "similarity score": 1,
        "NormalizedMainJobTitle": "Deputy Manager"
      },
      {
        "original title": "Assistant Manager",
        "normalized title": "Assistant Manager, Asset Management",
        "similarity score": 1,
        "NormalizedMainJobTitle": "Assistant Manager, Asset Management"
      },
      {
        "original title": "Senior Business Analyst",
        "normalized title": "Senior Manager Senior Business Analyst",
        "similarity score": 0.9765625,
        "NormalizedMainJobTitle": "Senior Manager Senior Business Analyst"
      },
      {
        "original title": "Business Analyst",
        "normalized title": "Business Analyst contractor",
        "similarity score": 1,
        "NormalizedMainJobTitle": "Business Analyst contractor"
      }
    ],
    "experienceNormData": {
      "overallExperience": 107,
      "skillExperience": [
        {
          "skills_name": "account",
          "totalMonths": 14,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "advance excel",
          "totalMonths": 81,
          "LastUsed": "04/2018"
        },
        {
          "skills_name": "allocation",
          "totalMonths": 18,
          "LastUsed": "04/2018"
        },
        {
          "skills_name": "allocations",
          "totalMonths": 18,
          "LastUsed": "04/2018"
        },
        {
          "skills_name": "alteryx",
          "totalMonths": 14,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "analytics",
          "totalMonths": 84,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "aod",
          "totalMonths": 17,
          "LastUsed": "09/2013"
        },
        {
          "skills_name": "audience measurement",
          "totalMonths": 35,
          "LastUsed": "09/2016"
        },
        {
          "skills_name": "automation",
          "totalMonths": 30,
          "LastUsed": "04/2018"
        },
        {
          "skills_name": "automation tools",
          "totalMonths": 11,
          "LastUsed": "03/2012"
        },
        {
          "skills_name": "big data",
          "totalMonths": 14,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "brand equity",
          "totalMonths": 14,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "budget",
          "totalMonths": 14,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "business planning",
          "totalMonths": 17,
          "LastUsed": "09/2013"
        },
        {
          "skills_name": "c",
          "totalMonths": 14,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "client management",
          "totalMonths": 42,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "clustering",
          "totalMonths": 14,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "coca cola",
          "totalMonths": 40,
          "LastUsed": "09/2013"
        },
        {
          "skills_name": "confluence",
          "totalMonths": 14,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "consumer insights",
          "totalMonths": 14,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "customer acquisition strategies",
          "totalMonths": 14,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "d3",
          "totalMonths": 35,
          "LastUsed": "09/2016"
        },
        {
          "skills_name": "data lakes",
          "totalMonths": 14,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "data strategies",
          "totalMonths": 14,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "deliveries",
          "totalMonths": 11,
          "LastUsed": "03/2012"
        },
        {
          "skills_name": "delivery",
          "totalMonths": 61,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "demand forecasting",
          "totalMonths": 18,
          "LastUsed": "04/2018"
        },
        {
          "skills_name": "designs",
          "totalMonths": 18,
          "LastUsed": "04/2018"
        },
        {
          "skills_name": "digital marketing",
          "totalMonths": 14,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "erosion",
          "totalMonths": 14,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "financial",
          "totalMonths": 35,
          "LastUsed": "09/2016"
        },
        {
          "skills_name": "financial forecasting",
          "totalMonths": 14,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "fine dining",
          "totalMonths": 11,
          "LastUsed": "03/2012"
        },
        {
          "skills_name": "fire",
          "totalMonths": 17,
          "LastUsed": "09/2013"
        },
        {
          "skills_name": "fmcg",
          "totalMonths": 31,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "forecasting",
          "totalMonths": 18,
          "LastUsed": "04/2018"
        },
        {
          "skills_name": "forecasting models",
          "totalMonths": 14,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "gap analysis",
          "totalMonths": 17,
          "LastUsed": "09/2013"
        },
        {
          "skills_name": "github",
          "totalMonths": 49,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "google analytics",
          "totalMonths": 35,
          "LastUsed": "09/2016"
        },
        {
          "skills_name": "governance",
          "totalMonths": 14,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "hana",
          "totalMonths": 14,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "hiring",
          "totalMonths": 84,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "hive",
          "totalMonths": 14,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "inventory",
          "totalMonths": 18,
          "LastUsed": "04/2018"
        },
        {
          "skills_name": "jira",
          "totalMonths": 14,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "jupyter",
          "totalMonths": 14,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "legal aspects",
          "totalMonths": 35,
          "LastUsed": "09/2016"
        },
        {
          "skills_name": "lifestyle",
          "totalMonths": 11,
          "LastUsed": "03/2012"
        },
        {
          "skills_name": "linear regression",
          "totalMonths": 18,
          "LastUsed": "04/2018"
        },
        {
          "skills_name": "market basket analysis",
          "totalMonths": 17,
          "LastUsed": "09/2013"
        },
        {
          "skills_name": "mentored",
          "totalMonths": 14,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "mysql",
          "totalMonths": 35,
          "LastUsed": "09/2016"
        },
        {
          "skills_name": "nielsen",
          "totalMonths": 28,
          "LastUsed": "09/2013"
        },
        {
          "skills_name": "omniture",
          "totalMonths": 14,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "optimizations",
          "totalMonths": 14,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "outlets",
          "totalMonths": 18,
          "LastUsed": "04/2018"
        },
        {
          "skills_name": "positioning",
          "totalMonths": 17,
          "LastUsed": "09/2013"
        },
        {
          "skills_name": "power bi",
          "totalMonths": 14,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "prediction",
          "totalMonths": 14,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "price",
          "totalMonths": 14,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "pricing strategy",
          "totalMonths": 35,
          "LastUsed": "09/2016"
        },
        {
          "skills_name": "product penetration",
          "totalMonths": 17,
          "LastUsed": "09/2013"
        },
        {
          "skills_name": "python",
          "totalMonths": 14,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "qsr",
          "totalMonths": 11,
          "LastUsed": "03/2012"
        },
        {
          "skills_name": "r",
          "totalMonths": 18,
          "LastUsed": "04/2018"
        },
        {
          "skills_name": "redesigning",
          "totalMonths": 14,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "regression",
          "totalMonths": 60,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "regression models",
          "totalMonths": 18,
          "LastUsed": "04/2018"
        },
        {
          "skills_name": "resourcing",
          "totalMonths": 32,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "retail",
          "totalMonths": 43,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "sales",
          "totalMonths": 35,
          "LastUsed": "09/2016"
        },
        {
          "skills_name": "sap",
          "totalMonths": 14,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "segmentation",
          "totalMonths": 28,
          "LastUsed": "09/2013"
        },
        {
          "skills_name": "sentiment analysis",
          "totalMonths": 17,
          "LastUsed": "09/2013"
        },
        {
          "skills_name": "shopper insights",
          "totalMonths": 25,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "sizing",
          "totalMonths": 18,
          "LastUsed": "04/2018"
        },
        {
          "skills_name": "spss",
          "totalMonths": 28,
          "LastUsed": "09/2013"
        },
        {
          "skills_name": "sql",
          "totalMonths": 14,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "stakeholder management",
          "totalMonths": 67,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "sysomos",
          "totalMonths": 17,
          "LastUsed": "09/2013"
        },
        {
          "skills_name": "tableau",
          "totalMonths": 31,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "targeting",
          "totalMonths": 17,
          "LastUsed": "09/2013"
        },
        {
          "skills_name": "teams",
          "totalMonths": 14,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "test",
          "totalMonths": 11,
          "LastUsed": "03/2012"
        },
        {
          "skills_name": "trade",
          "totalMonths": 14,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "vba",
          "totalMonths": 95,
          "LastUsed": "06/2019"
        },
        {
          "skills_name": "web",
          "totalMonths": 35,
          "LastUsed": "09/2016"
        }
      ]
    }
  }
}
```
