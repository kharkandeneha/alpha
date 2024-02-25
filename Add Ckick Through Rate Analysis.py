#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


import matplotlib as plt
import seaborn as sns


# In[3]:


df = pd.read_csv("C:\\Users\\HP\\Downloads\\click.csv")


# In[4]:


df.head()


# In[5]:


import plotly.graph_objects as go  #visualization libraries 
import plotly.express as px 
import plotly.io as pio 
pio.templates.default = "plotly_white" 


# ## The "Clicked on Ad" column contains 0 and 1 values , where 0 means not clicked and 1 means clicked . We will transform these values into "Yes" and "No".

# In[6]:


df['Clicked on Ad'] = df['Clicked on Ad'].map({0:'No',
                                              1:'Yes'})


# In[7]:


df.head(2)


# ## Now let's analyze the click through rate based on the time spent by the users on website.

# In[9]:


fig1 = px.box(df,
             x = "Daily Time Spent on Site",
             color = "Clicked on Ad",
             title = "Click Through Rate Based Time Spent on Site",
             color_discrete_map = {'Yes':'Blue',
                                  'No':'Red'})


# In[10]:


fig1.update_traces(quartilemethod = "exclusive") 
fig1.show() 


# ## Now we will analyze the click through rate based on the daily internet usage of the user 
# 

# In[14]:


fig = px.box(df,
            x = "Daily Internet Usage",
            color = "Clicked on Ad",
            title = "Clicked Through Rate Based on Daily Internet Usage ",
            color_discrete_map = {'Yes':'Blue','No':'Red'})


# In[15]:


fig.update_traces(quartilemethod = "exclusive") 
fig.show() 


# ## Now let's analyze thr click through rate based on the age of the user .

# In[31]:


fig2 = px.box(df,
             x = "Age",
             color = "Clicked on Ad",
             title = "Click Through Rate Based on Age",
             color_discrete_map = {'yes':'Black','No':'Red'})


# In[29]:


fig2.update_traces(quartilemethod = "exclusive")
fig2.show() 


# ## Now let's analyze the Click through rate based on the income of the users .

# In[32]:


fig3 = px.box(df,
             x = "Area Income",
             color = "Clicked on Ad",
             title = "Click Through Rate Based on Income",
             color_discrete_map = {'Yes':'Black' , 'No':'Red'})


# In[33]:


fig3.update_traces(quartilemethod = "exclusive")
fig3.show() 


# ## Calculating Click Through Rate of Ads

# In[17]:


df['Clicked on Ad'].value_counts()


# In[18]:


df.shape


# In[19]:


5083+4917


# In[21]:


click_through_rate_yes = 4917/10000 * 100
click_through_rate_yes


# In[22]:


click_through_rate_No = 5083/10000 * 100 
click_through_rate_No


# In[ ]:




