#!/usr/bin/env python
# coding: utf-8

# # Black friday dataset EDA and feature Engineering Cleaning and preparing the data for model training 

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')


# # Problem Statement
# A retail company “ABC Private Limited” wants to understand the customer purchase behaviour (specifically, purchase amount) against various products of different categories. They have shared purchase summary of various customers for selected high volume products from last month. The data set also contains customer demographics (age, gender, marital status, city_type, stay_in_current_city), product details (product_id and product category) and Total purchase_amount from last month.
# 
# Now, they want to build a model to predict the purchase amount of customer against various products which will help them to create personalized offer for customers against different products.

# In[4]:


#importing the dataset
df_train =pd.read_csv('C:\\Users\\SARVESH SURVE\\OneDrive\\Desktop\\data\\train.csv')


# In[5]:


df_train.head()


# In[6]:


df_test =pd.read_csv('C:\\Users\\SARVESH SURVE\\OneDrive\\Desktop\\data\\test.csv')


# In[7]:


df_test.head()


# In[8]:


df=df_train.append(df_test)
df.head()


# In[9]:


df.info()


# In[10]:


df.describe()


# In[11]:


df.drop(['User_ID'],axis=1,inplace=True)


# In[12]:


df.head(5)


# #making f = 0 and m = 1 by map() function

# In[13]:


#Handling a categorical feature Age
df['Gender']=df['Gender'].map({'F':0,'M':1})
df.head()


# In[14]:


#Handle categorical feature age


# In[15]:


df['Age'].unique()


# In[16]:


df['Age']=df['Age'].map({'0-17':1,'18-25':2,'26-35':3,'36-45':4,'46-50':5,'51-55':6,'55+':7})


# In[17]:


df.head()


# In[18]:


## Fixing categorical City_categorical


# In[19]:


df_city=pd.get_dummies(df['City_Category'],drop_first=True)


# In[20]:


df_city.head()


# In[21]:


df=pd.concat([df,df_city],axis=1)


# In[22]:


df.head()


# In[23]:


df.drop('City_Category',axis=1,inplace=True)


# In[24]:


df.head()


# In[25]:


##Missing values


# In[26]:


df.isnull().sum()


# In[27]:


##focus on replacing value


# In[28]:


df['Product_Category_2'].unique()


# In[29]:


df['Product_Category_2'].value_counts()


# In[30]:


## Replace the missing value with mode


# In[31]:


df['Product_Category_2'].mode()[0]


# In[32]:


df['Product_Category_2']=df['Product_Category_2'].fillna(df['Product_Category_2'].mode()[0])


# In[33]:


df['Product_Category_2'].isnull().sum()


# In[34]:


df['Product_Category_2'].value_counts()


# In[35]:


df['Product_Category_3'].mode()[0]


# In[36]:


df['Product_Category_3']=df['Product_Category_3'].fillna(df['Product_Category_3'].mode()[0])


# In[37]:


df['Product_Category_3'].isnull().sum()


# In[38]:


df.head()


# In[39]:


df.shape


# In[40]:


df['Stay_In_Current_City_Years'].unique()


# In[41]:


df['Stay_In_Current_City_Years']=df['Stay_In_Current_City_Years'].str.replace('+','')


# In[42]:


df.head()


# In[43]:


df.info()


# In[44]:


## covert object into integer


# In[45]:


df['Stay_In_Current_City_Years']=df['Stay_In_Current_City_Years'].astype(int)


# In[46]:


df.info()


# In[47]:


df['B']=df['B'].astype(int)
df['C']=df['C'].astype(int)


# In[48]:


df.info()


# In[49]:


##Visualization


# In[50]:


sns.barplot('Age','Purchase',hue='Gender',data=df)


# # Purchasing of men is high then women

# In[51]:


## Visualization of purchase with occupation
sns.barplot('Occupation','Purchase',hue='Gender',data=df)


# In[52]:


sns.barplot('Product_Category_1','Purchase',hue='Gender',data=df)


# In[53]:


sns.barplot('Product_Category_2','Purchase',hue='Gender',data=df)


# In[54]:


sns.barplot('Product_Category_3','Purchase',hue='Gender',data=df)


# In[55]:


##Feature Scaling
df_test=df[df['Purchase'].isnull()]


# In[56]:


df_train=df[~df['Purchase'].isnull()]


# In[57]:


X= df_train.drop('Purchase',axis=1)
X.head()


# In[85]:


y=df_train['Purchase']


# In[86]:


y


# In[ ]:




