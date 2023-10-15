#!/usr/bin/env python
# coding: utf-8

# 1. Create a dictionary and add key into it

# In[9]:


sozdik = {"faculty": "business school", "specialty": "Digital marketing", "id": 210201008}
ptint (sozdik)


# 2. Create multiple dictionaries and concatenate them

# In[6]:


artist = {"name": "Lana Del rey", "age": 38}
song = {"song name": "Cinnamon girl", "album": "Norman Fucking Rockwell"}
print (artist | song)


# 3. Create dictionary and find the maximum and minimum values

# In[10]:


score = {"Karakat": 299, "Inkar": 250, "Zarema": 302, "Adilkhan": 240}
print (max(score))
print (min(score))


# 4. Create a simple frozenset and try make some changes in it

# In[12]:


artist = {"name": "Lana Del rey", "age": 38} 
x = frozenset(artist)
x[1] = "Lana banana"


# 5. Create set, which contains 12 values with different types, and remove from it 3rd value. and add into set word 'python'

# In[27]:


tset = {12555, 25.5, '3bruh', 465, 5210201008, '6dora', 789, True, 9.5, '10kittys', 11.9, 121212}
tset.remove('3bruh')
tset.add('python')
print(tset)


# 6. Create 2 sets. Give examples for union and intersection

# In[37]:


set1 = {'okeokeoke', 'lalalala', 'bim', 'bam'}
set2 = {'alma', 'ketti', 'domalap', 'bim', 'bam'}
set3 = set1.union(set2)
set4 = set1.intersection(set2)
print(set3)
print(set4)


# 7. Create tuple and check item exists in a tuple or not
# 
# 

# In[41]:


albums = ('Blue Banisters', 'NFR', 'Born to Die', 'Honeymoon', 'Ultraviolence')

if 'Honeymoon' in albums:
    print('Honeymoon is alive and breathing')
else:
    print('no honeymoon here')


# 8. Create tuple with values i,n,t,r,o,d,u,c,t,i,o,n,t,t,o,p,y,t,h,o,n and slice it from 3 to 10

# In[43]:


subject = ('i', 'n', 't', 'r', 'o', 'd', 'u', 'c', 't', 'i', 'o', 'n', 't', 't', 'o', 'p', 'y', 't', 'h', 'o', 'n')
print(subject[2:10])


# 9. Give example for tuples concatination

# In[46]:


albums = ('Blue Banisters', 'NFR', 'Born to Die', 'Honeymoon', 'Ultraviolence')
albums2 = ('Blue jeans', 'Lust for life', 'COTCC')
print(albums + albums2)


# In[ ]:




