#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys


# In[3]:


def delCost(source, target, i, j):
    if source[i-1] == target[j-1]:
        return 0
    else:
        return 1
def insCost(source, target, i, j):
    if source[i-1] == target[j-1]:
        return 0
    else:
        return 1
def subCost(source, target, i, j):
    if source[i-1] == target[j-1]:
        return 0
    else:
        return 1


# In[4]:


def min_edit_distance(source, target):
    n = len(source)
    m = len(target)
    distance = []
    
    for i in range(n+1):
        distance.append([])
        for j in range(m+1):
            distance[i].append(None)
            
    
    #Initialization: the zeroth row and column is the distance from the empty string
    distance[0][0] = 0
    for i in range(1, n+1):
        distance[i][0] = distance[i-1][0]+1
    for j in range(1, m+1):
        distance[0][j] = distance[0][j-1]+1
    
    #Recurrence relation
    for i in range(1,n+1):
        for j in range(1,m+1):
            distance[i][j] = min([distance[i-1][j]+delCost(source, target, i, j),
                                  distance[i-1][j-1]+subCost(source, target, i, j),
                                  distance[i][j-1]+insCost(source, target, i, j)])
    
    print(distance[n][m])


# In[5]:


min_edit_distance(sys.argv[1],sys.argv[2])


# In[ ]:




