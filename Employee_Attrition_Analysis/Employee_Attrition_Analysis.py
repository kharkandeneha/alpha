#!/usr/bin/env python
# coding: utf-8

# ## Employee Attrition Analysis
# Employee Attrition Analysis is a type of behavioural analysis 
# where we study the behaviour and characteristics of the employees who 
# left the organization and compare their characteristics with the current employees 
# to find the employees who may leave the organization soon.

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df = pd.read_csv("C:\\Users\\HP\\Downloads\\Attrition.csv")


# In[3]:


df.head()


# In[4]:


df.shape


# In[5]:


import plotly.graph_objects as go #3-D visualization library
import plotly.io as pio
pio.templates.default = "plotly_white"


# In[7]:


# df.isnull().sum()


# In[10]:


attr_df = df[df['Attrition']=='Yes']


# In[11]:


attr_df.shape


# ## Calculate the attrition by Department

# In[14]:


attr_by_dpt = attr_df.groupby(['Department']).size().reset_index(name ="Count")
attr_by_dpt


# In[18]:


fig1 = go.Figure(data = [go.Pie(
    labels = attr_by_dpt['Department'],
    values = attr_by_dpt['Count'],
    hole = 0.4,
    marker = dict(colors = ['green','yellow',]),
    textposition = 'inside'
)])
fig1.update_layout(title = "Attrition By Department")
fig1.show()


# ## Attrition By Eduction Field

# In[19]:


attr_by_edu = attr_df.groupby(['EducationField']).size().reset_index(name="Count")
attr_by_edu


# In[20]:


fig1 = go.Figure(data = [go.Pie(
    labels = attr_by_edu['EducationField'],
    values = attr_by_edu['Count'],
    hole = 0.4 , 
    marker = dict(colors = ['green','yellow']),
    textposition = 'inside'
)])

fig1.update_layout(title="Attrition By EducationField")
fig1.show()


# ## Now let's have a look at the percentage of attrition by Number of Years at the Company

# In[21]:


attr_by_comp = attr_df.groupby(['YearsAtCompany']).size().reset_index(name="Count")
attr_by_comp


# In[22]:


attr_by_promo = attr_df.groupby(['YearsSinceLastPromotion']).size().reset_index(name="Count")
attr_by_promo


# In[23]:


df.columns


# ## Now let's analyze attrition by Gender

# In[24]:


attr_by_gender = attr_df.groupby(['Gender']).size().reset_index(name="Count")
attr_by_gender


# In[25]:


fig1 = go.Figure(data = [go.Pie(
    labels = attr_by_gender['Gender'],
    values = attr_by_gender['Count'],
    hole = 0.4 , 
    marker = dict(colors = ['green','yellow']),
    textposition = 'inside'
)])

fig1.update_layout(title="Attrition By Gender")
fig1.show()


# ## Now let's have a look at the attrition by analyzing the relationship between Monthly Income And the Age of the Employees .

# In[28]:


import plotly.express as px 


# In[29]:


fig = px.scatter(df , 
                x = "Age",
                y = "MonthlyIncome",
                color = "Attrition",
                trendline = "ols")
fig.update_layout(title="Age Vs Monthly Income By Attrition")
fig.show() 


# In[ ]:


# We can see that as the age of the person increases ,
# monthly Income Increases . We can also see a high rate of attrition
# among the employees with low monthly incomes .

