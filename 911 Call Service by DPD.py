
# coding: utf-8

# # DPD: 911 Calls for Service

# # Introduction

# This data represents all the 911 police emergency calls for service response and officer-initiated call for service in the City of Detroit from the beginning September 20, 2016 - present. People call 911 to request police services during emergency. Calls for which officer was initiated include traffic stops, street investigations and other policing activities like observing crimes in progress where the police officers were initiated. This data includes the responding agency, unit, call type and category of each call. The table includes all the calls taken, dispatch time, travel time and total response time for all the calls serviced by a police agency.

# # Importing

# In[64]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[65]:


import os


# In[66]:


import os
path="/Users/Anirudh MVR"
os.chdir(path)


# In[67]:


os.getcwd()


# In[68]:


df = pd.read_csv('data.csv', low_memory=False)


# # Data Wrangling

# In[82]:


df.head()


# Step 1: Checking null-values

# In[83]:


print(df.columns[df.isnull().any()].tolist())


# Step 2: Removing unnecessary columns

# In[84]:


df.drop(df.columns[[0,1]], axis=1, inplace=True)


# Step 3: Removal of null-values

# In[69]:


df_new = df.dropna()


# In[70]:


df_new.head()


# In[77]:


df_new.tail()


# # Data Description

# In[78]:


df_new.describe()


# In[73]:


df_new.info()


# In[79]:


df_new.shape


# In[80]:


df_new.columns


# In[76]:


df_new.ndim


# # Exploratory Data Analysis

# In[203]:


call_description = df_new['Call Description'].value_counts()


# In[204]:


call_description


# In[87]:


vals = df_new['Neighborhood'].value_counts()


# In[88]:


top_ten_neighborhood = vals[0:9]


# In[89]:


top_ten_neighborhood


# # Top 10 Neighborhood

# In[123]:


plt.figure(figsize=(8, 5),)
ax = top_ten_neighborhood.plot.bar(width = 0.8)
for i, v in top_ten_neighborhood.reset_index().iterrows():
    ax.text(i, v.Neighborhood + 0.2, v.Neighborhood, color = 'blue')
plt.title('Top 10 Neighborhood')


# In[119]:


vals_1 = df_new['Call Description'].value_counts()


# In[120]:


top_ten_calls = vals_1[0:9]


# In[121]:


top_ten_calls


# # Top 10 Call Descriptions

# In[122]:


plt.figure(figsize=(10, 6),)
ax = top_ten_calls.plot.bar(width = 0.8)
for i, v in top_ten_calls.reset_index().iterrows():
    ax.text(i, v['Call Description'] + 0.2, v['Call Description'], color = 'blue')
plt.title('Top 10 Call Descriptions')


# # Officers Inititation

# In[95]:


vals_2 = df_new['Officer Initiated'].value_counts()


# In[96]:


vals_2


# In[117]:


plt.figure(figsize=(10, 6),)
ax = vals_2.plot.bar(width = 0.5)
for i, v in vals_2.reset_index().iterrows():
    ax.text(i, v['Officer Initiated'] + 0.2, v['Officer Initiated'], color = 'blue')
plt.title('Officers Inititation')


# # Removal of unsupported characters

# In[47]:


remove_comma = [x.strip(',') for x in df_new['Total Response Time']]


# In[40]:


remove_comma_1 = [y.strip(',') for y in df_new['Intake Time']]


# In[41]:


remove_comma_2 = [y.strip(',') for y in df_new['Dispatch Time']]


# In[42]:


remove_comma_3 = [y.strip(',') for y in df_new['Travel Time']]


# In[43]:


remove_comma_4 = [y.strip(',') for y in df_new['Time On Scene']]


# In[44]:


remove_comma_5 = [y.strip(',') for y in df_new['Total Time']]


# In[45]:


len(remove_comma_1)


# # Number of calls per year

# In[110]:


plt.figure(figsize=(20,10))
plt.ylabel('Number of Calls', fontsize=20)
plt.xlabel('Year', fontsize=20)
plt.rcParams['ytick.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 14
plt.title('Number of Calls per year')
df_new.groupby([df_new.index.year]).size().plot(kind='bar', style=["seaborn-whitegrid"])
plt.show()


# In[101]:


plt.figure(figsize=(12, 6))
df_new.resample('Y').size().plot(legend=False)
plt.title('Number of call per year (2016 - 2018)')
plt.xlabel('Years')
plt.ylabel('Number of calls')
plt.show()


# # Average number of calls per month

# In[98]:


df_new['Call Time'] = pd.to_datetime(df_new['Call Time'], format = '%m/%d/%Y %I:%M:%S %p')
df_new.index = pd.DatetimeIndex(df_new['Call Time'])


# In[115]:


plt.figure(figsize=(20,10))
plt.ylabel('Average number of Calls', fontsize=20)
plt.xlabel('Month of the year', fontsize=20)
#plt.rcParams['ytick.labelsize'] = 14
#plt.rcParams['xtick.labelsize'] = 14
plt.title('Average number of Calls by month of the year')
df_new.groupby([df_new.index.month]).size().plot(kind='bar', style=["seaborn-whitegrid"])
plt.show()


# In[111]:


plt.figure(figsize=(12, 6))
df_new.resample('M').size().plot(legend=False)
plt.title('Average number of calls per month')
plt.xlabel('Month')
plt.ylabel('Number of calls')
plt.show()


# # Average number of calls per day

# In[106]:


plt.figure(figsize=(20,10))
plt.ylabel('Number of Calls', fontsize=20)
plt.xlabel('Days', fontsize=20)
plt.rcParams['ytick.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 14
plt.title('Number of Calls by Days')
df_new.groupby([df_new.index.day]).size().plot(kind='bar', style=["seaborn-whitegrid"])
plt.show()


# # Correlation

# In[114]:


from sklearn.preprocessing import Normalizer
df_sub = dff[['Intake Time','Dispatch Time', 'Travel Time', 'Total Response Time', 'Time On Scene']]
df_sub.dropna(inplace=True)
df_nor = Normalizer().fit_transform(df_sub)
corr = pd.DataFrame(df_nor).corr()

sns.heatmap(corr, 
           xticklabels=df_sub.columns.values,
           yticklabels=df_sub.columns.values)


# # Google Map Plotting

# In[56]:


from gmplot import gmplot


# In[57]:


lat = df_new['Latitude']
long = df_new['Longitude']


# In[58]:


gmap = gmplot.GoogleMapPlotter(42.3314, -83.0458, 8)
gmap.heatmap(lat, long)


# In[59]:


gmap.draw('my_map.html')


# # Summary

# The name of the dataset is “DPD: 911 Calls for Service”, which has been fetched from the following URL: https://data.detroitmi.gov/Public-Safety/DPD-911-Calls-for-Service-September-20-2016-Presen/wgv9-drfc
# 
# This raw dataset had 1.17 million rows and 25 columns initially. After the data cleaning, the dataset has 441576 rows and 25 columns. This data represents all the 911 police emergency calls for service response and officer-initiated call for service in the City of Detroit from the beginning September 20, 2016 - present.
# 
# People call 911 to request police services during emergency. Calls for which officer was initiated include traffic stops, street investigations and other policing activities like observing crimes in progress where the police officers were initiated. This data includes the responding agency, unit, call type and category of each call. The table includes all the calls taken, dispatch time, travel time and total response time for all the calls serviced by a police agency.
# 
# The first visualization shows the top ten neighborhood from where the highest number of calls were made. In this list of top ten, the highest number of calls were made from “Midtown” and the least number of calls were made from “Warren Ave Community”.
# 
# The second visualization shows the top ten reasons for people calling the 911 service. In this list of top ten, the highest number of calls were made for “Traffic Stop” and the least number of calls were made for “Remarks”.
# 
# The third visualization shows the number times, officers being initiated and not being initiated. Officers were initiated for 301088 calls and officers  were not initiated for 140488 calls.
# 
# The fourth visualization shows the number of calls per year.
# 
# The fifth visualization shows the average number of calls per month.
# 
# The sixth visualization shows the average number calls on a daily basis.
# 
# The seventh visualization shows the correlation. 
