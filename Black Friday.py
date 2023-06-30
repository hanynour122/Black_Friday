#!/usr/bin/env python
# coding: utf-8

# In[113]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl


# In[3]:


df=pd.read_csv(r"C:\Users\Hany\Downloads\archive (5)\train.csv")


# In[4]:


df


# In[35]:


df.describe()


# In[5]:


df.isnull().sum()


# In[17]:


m_category2=df["Product_Category_2"].mean()


# In[18]:


df["Product_Category_2"]=df["Product_Category_2"].fillna(m_category2)


# In[23]:


m_category3=df["Product_Category_3"].mean()


# In[29]:


df["Product_Category_3"]=df["Product_Category_3"].fillna(m_category3)


# In[67]:


df.head()


# In[32]:


df.isnull().sum()


# In[44]:


df=df.drop(["User_ID"],axis=1)


# In[65]:


count_male=df["Gender"][df["Gender"]=="M"].count()
count_male


# In[66]:


count_female=df["Gender"][df["Gender"]=="F"].count()
count_female


# In[91]:


#df.groupby(["Occupation","Purchase"],axis=0).sum()


# In[119]:


groped=df[['Purchase']].groupby(df['Occupation'],axis=0).sum()
groped


# In[98]:


groped1=df[['Purchase']].groupby(df['City_Category'],axis=0).sum()
groped1


# In[120]:


groped2=df[['Purchase']].groupby(df['Age'],axis=0).sum()
groped2


# In[107]:


df.dtypes


# In[ ]:





# In[ ]:





# In[ ]:




