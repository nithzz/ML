#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np


# In[4]:


movies = pd.read_csv(r'C:\Users\Nithya\Documents\ML\ml-100k\u.item',sep="|",encoding="latin-1")
movies.head()


# In[5]:





# In[8]:


ratings = pd.read_csv(r'C:\Users\Nithya\Documents\ML\ml-100k\u.data',sep="\t",usecols=['userId','itemId','rating'])
ratings.head()


# In[12]:


row=max(ratings.userId)


# In[13]:


col=max(ratings.itemId)


# In[23]:


arr=np.zeros([row,col],dtype=int)


# In[24]:


print(arr)


# In[27]:


for i in range(0,100000):
    arr[ratings.userId[i]-1][ratings.itemId[i]-1]=ratings.rating[i]


# In[28]:


print(arr)


# In[29]:


arr[0]


# In[47]:


euclArr = np.zeros([row,row],dtype=object)
        


# In[72]:





# In[81]:


for i in range(0,row):
    for j in range(0,row):
        dist = np.linalg.norm(arr[i]-arr[j])
        euclArr[i][j] = (dist,j)


# In[82]:


for i in range(0,row):
    euclArr[i].sort(axis=0)


# In[83]:


euclArr


# In[84]:


k_val = eval(input("value of k : "))


# In[89]:


tmpList = []
for i in range(0,20):
    tmpList+=[euclArr[0][i]]
  


# In[90]:


tmpList


# In[ ]:


movRating=0
for i in range(0,col):
    if(arr[0][i] == 0):
        for j in range(0,k_val):
            

