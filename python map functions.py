#!/usr/bin/env python
# coding: utf-8

# In[2]:


##### python map functions ####

# map(function, iterable_1, iterable_2, ...iterable_N)

# first define the transformation function
def reverse(str):
    string = " "
    for i in str:
        string = i + string
    return string

# the list of words
words = ['Data science', 'Ayieko', 'Jupyter', 'Coding']

# apply the map() function
reversed_words = map(reverse, words) # returns the map object

print(reversed_words)


# In[3]:


# convert map object to list
print('reversed_words:', list(reversed_words))


# In[ ]:




