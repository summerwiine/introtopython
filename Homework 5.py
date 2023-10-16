#!/usr/bin/env python
# coding: utf-8

# 1. Get the Python version

# In[1]:


from platform import python_version

print(python_version())


# 2. Create a program for given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!"

# In[ ]:


name = "Bob"
print("Hello " + name + "!")


# 3. Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

# In[8]:


name = input("What is your name? ")
age = int(input("How old are you? enter a number "))
hundred_years = ((100-age) + 2023)
print ('Hello %s. You are %s years old. You will turn 100 years old in %s.' % (name, age, hundred_years))


# In[ ]:




