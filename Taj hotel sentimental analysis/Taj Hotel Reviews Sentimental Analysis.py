#!/usr/bin/env python
# coding: utf-8

# # Project(Taj Hotel Reviews Sentiment Analysis)
# Whenver we are looking for hotels for vacation or travel, we always 
# prefer a hotel known for its services. The best way to find out whether a
# hotel is right for you or not is to find out what people are saying about
# the hotel who have stayed there before. Now it is very dificult to read 
# the experience of each person who has given their opinion on the services of the hotel.

# In[17]:


import numpy as np
import pandas as pd


# In[18]:


df = pd.read_csv("C:\\Users\\HP\\Downloads\\hotel.csv")


# In[19]:


df.head()


# In[20]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[21]:


ratings = df["Rating"].value_counts()
ratings


# In[22]:


numbers = ratings.index
numbers


# In[23]:


quantity = ratings.values
quantity


# In[24]:


custom_colors = ['skyblue','yellowgreen','tomato','blue','red']
plt.figure(figsize = (5,5))
plt.pie(quantity, labels = numbers,colors = custom_colors)
central_circle = plt.Circle((0,0) , 0.5 , color = 'white')
fig = plt.gcf()
fig.gca().add_artist(central_circle)
plt.rc('font',size = 12)
plt.title("Taj Hotel Reviews" , fontsize = 20)
plt.show()


# In[25]:


import nltk
nltk.download('vader_lexicon')


# In[32]:


from nltk.sentiment.vader import SentimentIntensityAnalyzer 


# In[33]:


sentiments = SentimentIntensityAnalyzer()


# In[34]:


df['Positive'] = [sentiments.polarity_scores(i)['pos'] for i in df['Review']]
df['Negative'] = [sentiments.polarity_scores(i)['neg'] for i in df['Review']]
df['Neutral'] = [sentiments.polarity_scores(i)['neu'] for i in df['Review']]


# In[35]:


df.head() 


# # According to the reviews , hotel guests seem satisfied with the services .Now let's have a look at how most people think about hotel servicesbased on the sentiment of their reviews 

# In[36]:


x = sum(df['Positive'])
y = sum(df['Negative'])
z = sum(df['Neutral'])


# In[37]:


print("Total Positive:" , x)
print("Total Negative:" , y)
print("Total Neutral:" , z)


# In[39]:


def sentiment_score(a,b,c):
    if(a>b) and (a>c):
        print("Positive😍")
    elif(b>a) and (b>a):
        print("Negative😣")
    else:
        print("Neutral😐")
sentiment_score(x,y,z)


# In[ ]:





# In[ ]:




