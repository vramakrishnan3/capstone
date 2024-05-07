

# Pandas is a software library written for the Python programming language for data manipulation and analysis.
import pandas as pd
#NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays
import numpy as np

# Load spacex dataset from last section
df=pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_1.csv")
df.head(10)

#Identify and calculate the percentage of the missing values in each attribute
df.isnull().sum()/len(df)*100

# Identify which columns are numerical and categorical:
df.dtypes

# TASK 1: Calculate the number of launches on each site
df['LaunchSite'].value_counts()

#CCAFS SLC 40    55
#KSC LC 39A      22
#VAFB SLC 4E     13
#Name: LaunchSite, dtype: int64

#TASK 2: Calculate the number and occurrence of each orbit
# Apply value_counts on Orbit column
df['Orbit'].value_counts()

#GTO      27
#ISS      21
#VLEO     14
#PO        9
#LEO       7
#SSO       5
#MEO       3
#ES-L1     1
#HEO       1
#SO        1
#GEO       1
#Name: Orbit, dtype: int64

#TASK 3: Calculate the number and occurence of mission outcome of the orbits
landing_outcomes = df['Outcome'].value_counts()
landing_outcomes

#True ASDS      41
#None None      19
#True RTLS      14
#False ASDS      6
#True Ocean      5
#False Ocean     2
#None ASDS       2
#False RTLS      1
#Name: Outcome, dtype: int64


for i,outcome in enumerate(landing_outcomes.keys()):
    print(i,outcome)

#0 True ASDS
#1 None None
#2 True RTLS
#3 False ASDS
#4 True Ocean
#5 False Ocean
#6 None ASDS
#7 False RTLS

#We create a set of outcomes where the second stage did not land successfully:

bad_outcomes=set(landing_outcomes.keys()[[1,3,5,6,7]])
bad_outcomes

#{'False ASDS', 'False Ocean', 'False RTLS', 'None ASDS', 'None None'}


#TASK 4: Create a landing outcome label from Outcome column
#Using the Outcome, create a list where the element is zero if the corresponding row in Outcome is in the set bad_outcome; otherwise, it's one. Then assign it to the variable landing_class:

# landing_class = 0 if bad_outcome
# landing_class = 1 otherwise

def categorize_outcome(outcome):
    if bad_outcomes.__contains__(outcome):
        return 0
    else:
        return 1
    
landing_class=df['Outcome'].map(categorize_outcome)
landing_class

df['Class']=landing_class
df[['Class']].head(8)

#We can use the following line of code to determine the success rate:
df["Class"].mean()

#0.6666666666666666


df.to_csv("dataset_part_2.csv", index=False)


