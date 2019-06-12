#!/usr/bin/env python
# coding: utf-8

# In[52]:


import urllib3
import facebook
import requests
import pandas as pd


# In[24]:


token = 'EAAgOQRZBhF5oBANWZCJnVoWtJ0mnQmdZAKzIIz3jpEvNAb30zT8dygUWDYdxhZAZCU7eZA3do7G8wxOWqzATsnk9Qq7rv4H7u4EBZBuMJ2RaTtFmg17RUaC8VNcYFNcyG9v5mztJ9sIrjMVPAzk7cFisEYVkqFpGuDqUjBqBht9nwZDZD'
user = '100002345472592'


# In[34]:


graph = facebook.GraphAPI(access_token=token, version = 2.8)
events = graph.request('me?fields=birthday')

args = {'fields' : 'birthday,gender' }

friends = graph.get_object("me",**args)


# In[35]:


print(friends)


# In[33]:


print(events)


# In[36]:


friends['birthday']


# In[56]:


birthday = requests.get('https://graph.facebook.com/v2.7/' + 'me?fields=name,email,gender,birthday&access_token='+token) 


# In[57]:


birthday_json = birthday.json() #parses json and returns dict


# In[58]:


birthday_json


# In[60]:


import csv
my_dict = birthday_json
with open('test.csv', 'w') as f:
    for key in my_dict.keys():
        f.write("%s,%s\n"%(key,my_dict[key]))


# In[59]:


birthday

