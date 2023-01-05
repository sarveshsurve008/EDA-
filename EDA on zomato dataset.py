#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[15]:


df =pd.read_csv('C:\\Users\\SARVESH SURVE\\OneDrive\\Desktop\\data\\zomato.csv',encoding="latin1")


# In[17]:


df.head()


# In[18]:


df.columns


# In[19]:


df.info()


# In[20]:


df.describe()


# In[21]:


df.isnull().sum()


# #code for seeing missing values in columns
# 

# In[26]:


[features for features in df.columns if df[features].isnull().sum()>0]


# In[91]:


sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap="viridis")


# In[28]:


df_country=pd.read_excel("C:\\Users\\SARVESH SURVE\\OneDrive\\Desktop\\data\\Country-code.xlsx")


# In[29]:


df_country.head()


# In[30]:


df.columns


# In[32]:


final_df=pd.merge(df,df_country,on='Country Code',how="left")


# In[34]:


final_df.head(2)


# In[35]:


final_df.dtypes


# In[37]:


final_df.Country.value_counts()


# In[38]:


country_names =final_df.Country.value_counts().index


# In[39]:


country_names


# In[40]:


country_val=final_df.Country.value_counts().values


# In[41]:


country_val


# In[49]:


# pie chart - top 3 country that uses zomato
plt.pie(country_val[:3],labels=country_names[:3],autopct='%1.2f%%')


# observation : zomato maximum transaction is from INDIA and that US then UK

# In[50]:


final_df.columns


# In[82]:


rating=final_df.groupby(['Aggregate rating','Rating color', 'Rating text']).size().reset_index().rename(columns={0:'Rating count'})


# # observation
# 1. when rating is between 4.5 to 4.9 ----> Excellent
# 2. when rating is between 4.0 to 4.4-----> very good
# 3. when rating is between 3.5 to 3.9-----> good
# 4. when rating is between 2.5 to 3.4-----> Average
# 5. when rating is between 1.8 to 2.4-----> poor
# 

# In[83]:


rating


# In[84]:


rating.head()


# In[90]:


plt.rcParams['figure.figsize']= (12,6)
sns.barplot(x='Aggregate rating',y='Rating count',data=rating)


# In[97]:


sns.barplot(x='Aggregate rating',y='Rating count', hue='Rating color',data=rating,palette=['blue','red','orange','yellow','green','green'])


# ## observation 
# 1. Not rated count is very high
# 2. Maximum number of rating is between 2.5 to 3.5

# In[99]:


## count plot
sns.countplot(x='Rating color',data= rating,palette=['blue','red','orange','yellow','green','green'])


# In[100]:


## find the countries names that has given zero rating


# In[108]:


final_df[final_df['Rating color']=='White'].groupby('Country').size().reset_index()


# In[109]:


final_df.groupby(['Aggregate rating','Country']).size().reset_index().head(5)


# # observation
# 1. maximum number of  0 rating are from INDIAN customers

# Finding out which currency is used by which country?
# 

# In[110]:


final_df[['Country','Currency']].groupby(['Country','Currency']).size().reset_index()


# Q finding which countries of online deliveries?

# In[111]:


final_df[final_df['Has Online delivery'] =="Yes"].Country.value_counts()


# In[112]:


final_df.groupby(["Country","Has Online delivery"]).size().reset_index()


# 1. online delivery is available in INDIA and US

# In[113]:


## creating pie chart for cities


# In[115]:


final_df.City.value_counts().index


# In[122]:


city_values=final_df.City.value_counts().values
city_labels=final_df.City.value_counts().index


# In[125]:


plt.pie(city_values[:5],labels=city_labels[:5],autopct='%1.2f%%')


# In[ ]:




