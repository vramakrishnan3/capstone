

#Assignment: SQL Notebook for Peer Assignment

!pip install sqlalchemy==1.3.9

#Please uncomment and execute the code below if you are working locally.
#!pip install ipython-sql

%load_ext sql

import csv, sqlite3

con = sqlite3.connect("my_data1.db")
cur = con.cursor()

!pip install -q pandas==1.1.5

%sql sqlite:///my_data1.db

import pandas as pd
df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/data/Spacex.csv")
df.to_sql("SPACEXTBL", con, if_exists='replace', index=False,method="multi")

# Below to remove blank rows from table
%sql create table SPACEXTABLE as select * from SPACEXTBL where Date is not null

#Task 1: Display the names of the unique launch sites in the space mission
%sql select DISTINCT(Launch_Site) from SPACEXTBL

#Task 2: Display 5 records where launch sites begin with the string 'CCA'
%sql select * from SPACEXTBL where Launch_site like 'CCA%' LIMIT 5

#Task 3: Display the total payload mass carried by boosters launched by NASA (CRS)
%sql select SUM(PAYLOAD_MASS__KG_) from SPACEXTBL where Customer = 'NASA (CRS)'

#Task 4: Display average payload mass carried by booster version F9 v1.1
%sql select AVG(PAYLOAD_MASS__KG_) from SPACEXTBL where Booster_Version like '%F9%v1.1%'

#Task 5: List the date when the first succesful landing outcome in ground pad was acheived
%sql select MIN(Date) from SPACEXTBL where Landing_Outcome = 'Success (ground pad)'

#Task 6: List the names of the boosters which have success in drone ship and have payload mass greater than 4000 but less than 6000
%sql select DISTINCT(Booster_Version) from SPACEXTBL where Landing_Outcome = 'Success (drone ship)' and PAYLOAD_MASS__KG_ > 4000 and PAYLOAD_MASS__KG_ < 6000

#Task 7: List the total number of successful and failure mission outcomes
%sql select Count(1), case when MISSION_OUTCOME like 'Success%' then 'Sucess' else 'Failure' end as OUTCOME from SPACEXTBL GROUP BY case when MISSION_OUTCOME like 'Success%' then 'Sucess' else 'Failure' end


#Task 8: List the names of the booster_versions which have carried the maximum payload mass. Use a subquery
%sql select booster_version, PAYLOAD_MASS__KG_ from SPACEXTBL o where PAYLOAD_MASS__KG_ = (select max(i.PAYLOAD_MASS__KG_) from SPACEXTBL i where SUBSTRING (i.booster_version, 0, LENGTH( i.booster_version)) = SUBSTRING (o.booster_version, 0, LENGTH( o.booster_version) ) )

#Task 9: List the records which will display the month names, failure landing_outcomes in drone ship ,booster versions, launch_site for the months in year 2015.
%sql select substr(Date, 6,2), landing_outcome, booster_version, launch_site  from SPACEXTBL where Landing_Outcome in ('Failure (drone ship)','Precluded (drone ship)') and substr(Date,0,5) = '2015'

#Task 10: Rank the count of landing outcomes (such as Failure (drone ship) or Success (ground pad)) between the date 2010-06-04 and 2017-03-20, in descending order.
%sql select count(landing_outcome), landing_outcome from SPACEXTBL where date(substr(Date,0,5) || '-' || substr(Date, 6,2) || '-' || substr(Date, 9, 2)) between DATE('2010-06-04') and DATE('2017-03-20') group by landing_outcome order by count(landing_outcome) desc








