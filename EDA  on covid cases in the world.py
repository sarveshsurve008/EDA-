#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


data = pd.read_csv("C:\\Users\\SARVESH SURVE\\OneDrive\\Desktop\\data\\us_states_covid19_daily.csv")


# In[9]:


data.info()


# In[10]:


data.head()


# In[11]:


data.describe()


# In[12]:


data['state'].value_counts()


# In[13]:


print(data['date'].unique())

print (data['state'].nunique() )


# In[14]:


data['date']= data['date'].astype('str')


# In[15]:


data['date'] = pd.to_datetime(data['date'])
print (data['date'])
data.head()


# In[16]:


data['month'] = data['date'].dt.month
data['year'] = data['date'].dt.year


# In[17]:


data.head()


# In[18]:


cond = data['month']== 11
data_11 = data[cond]
data_11.info() 


# In[19]:


data_11.head(10)

data_11g = data_11.groupby(['state','month']).mean()


# In[20]:


data_11g.head()


# In[21]:


data_11short= data_11g.iloc[:,[0.2]]


data_11short = data_11short.round(1)


# In[22]:


data_11short.head()


# In[23]:


data_11short2 = data_11g.loc[:,'positive']
data_11short2 = data_11short2.round(1)
data_11short2.head()


# In[24]:


data_11short2.round(1)

data_11short2.head()


# In[25]:


data_11short2.duplicated()


# In[26]:


data_11short2.head(11)

