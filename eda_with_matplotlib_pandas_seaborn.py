
import piplite
await piplite.install(['numpy'])
await piplite.install(['pandas'])
await piplite.install(['seaborn'])

# pandas is a software library written for the Python programming language for data manipulation and analysis.
import pandas as pd
#NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays
import numpy as np
# Matplotlib is a plotting library for python and pyplot gives us a MatLab like plotting framework. We will use this in our plotter function to plot data.
import matplotlib.pyplot as plt
#Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics
import seaborn as sns

#First, let's read the SpaceX dataset into a Pandas dataframe and print its summary

from js import fetch
import io

URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv"
resp = await fetch(URL)
dataset_part_2_csv = io.BytesIO((await resp.arrayBuffer()).to_py())
df=pd.read_csv(dataset_part_2_csv)
df.head(5)


# First, let's try to see how the FlightNumber (indicating the continuous launch attempts.) and Payload variables would affect the launch outcome.

sns.catplot(y="PayloadMass", x="FlightNumber", hue="Class", data=df, aspect = 5)
plt.xlabel("Flight Number",fontsize=20)
plt.ylabel("Pay load Mass (kg)",fontsize=20)
plt.show()

### TASK 1: Visualize the relationship between Flight Number and Launch Site
# Plot a scatter point chart with x axis to be Flight Number and y axis to be the launch site, and hue to be the class value
sns.catplot(y="LaunchSite", x="FlightNumber", hue="Class", data=df, aspect = 5)
plt.xlabel("Flight Number",fontsize=20)
plt.ylabel("Launch Site",fontsize=20)
plt.show()

### TASK 2: Visualize the relationship between Payload and Launch Site
# Plot a scatter point chart with x axis to be Pay Load Mass (kg) and y axis to be the launch site, and hue to be the class value
sns.catplot(y="LaunchSite", x="PayloadMass", hue="Class", data=df, aspect = 5)
plt.xlabel("Pay load Mass (kg)",fontsize=20)
plt.ylabel("Launch Site", fontsize=20)
plt.show()

### TASK  3: Visualize the relationship between success rate of each orbit type
# HINT use groupby method on Orbit column and get the mean of Class column
series_mean=df.groupby('Orbit')['Class'].mean()
df_mean = pd.DataFrame(series_mean)
sns.barplot(x='Orbit', y='Class', data=df_mean)

### TASK  4: Visualize the relationship between FlightNumber and Orbit type
# Plot a scatter point chart with x axis to be FlightNumber and y axis to be the Orbit, and hue to be the class value

ax = sns.scatterplot(x='FlightNumber', y='Orbit', data=df, hue='Class')
ax.set(xlabel='Flight Number', ylabel='Orbit Type')

### TASK  5: Visualize the relationship between Payload and Orbit type
# Plot a scatter point chart with x axis to be Payload and y axis to be the Orbit, and hue to be the class value
ax = sns.scatterplot(x='PayloadMass', y='Orbit', data=df, hue='Class')
ax.set(xlabel='Payload', ylabel='Orbit Type')

### TASK  6: Visualize the launch success yearly trend
# A function to Extract years from the date 
year=[]
def Extract_year():
    for i in df["Date"]:
        year.append(i.split("-")[0])
    return year
Extract_year()
df['Date'] = year
df.head()

# Plot a line chart with x axis to be the extracted year and y axis to be the success rate
df_line_series_mean = df.groupby('Date')['Class'].mean()
df_line_mean = pd.DataFrame(df_line_series_mean)

df_line_mean.reset_index(inplace=True)
#df_line_mean[['Date','Class']].head(6)

plt.plot(df_line_mean["Date"], df_line_mean["Class"])
plt.show()



### TASK  7: Create dummy variables to categorical columns
features = df[['FlightNumber', 'PayloadMass', 'Orbit', 'LaunchSite', 'Flights', 'GridFins', 'Reused', 'Legs', 'LandingPad', 'Block', 'ReusedCount', 'Serial']]
features.head()

#Use the function <code>get_dummies</code> and <code>features</code> dataframe to apply OneHotEncoder to the column <code>Orbits</code>, <code>LaunchSite</code>, #<code>LandingPad</code>, and <code>Serial</code>. Assign the value to the variable <code>features_one_hot</code>, display the results using the method head. Your #result dataframe must include all features including the encoded ones.

features_one_hot=pd.get_dummies(features, columns=['Orbit','LaunchSite','LandingPad','Serial'], prefix=['Orbit','LaunchSite','LandingPad','Serial'])
features_one_hot.head()


### TASK  8: Cast all numeric columns to `float64`

# HINT: use astype function
features_one_hot = features_one_hot.astype(float)
features_one_hot.to_csv('dataset_part_3.csv', index=False)








