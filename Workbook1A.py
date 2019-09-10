#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
Location = "C:\Users\chris\Documents\Python\datasets\Alabama.csv"
#add headers to imported data
df = pd.read_csv(Location)
df.head()

