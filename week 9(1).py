#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
list=['1','2','3','4','5']
array_list=np.array(object=list)


# In[2]:


array_list


# Q-1 Is there any difference in the data type of variable list and array_list ? If there is then write a code to print the data types of both the variables.

# Ans-1 In python both 'list_' and 'array_list' would be treated as variable names and they can refer to objects of any data type, 
#       depending on what you assign to them .The names themselves don't imply any apecific data type.

# In[1]:


list_=[1,2,3]
array_list=[4,5,6]


# In[3]:


list_
type(list_)


# In[4]:


array_list


# In[5]:


type(array_list)


# Q-2. Write a code to print the data type of each and every element of both the variables list_ and 
# arra_list.

# In[3]:


list=['1','2','3','4','5']
array_list=np.array(object=list)


# In[4]:


array_list


# In[5]:


type(list)


# In[6]:


type(array_list)


# Q3. Considering the following changes in the variable, array_list:
# 
# array_list = np.array(object = list_, dtype = int)
# 
# Will there be any difference in the data type of the elements present in both the variables, list_ and 
# arra_list? If so then print the data types of each and every element present in both the variables, list_ 
# and arra_list.
# 
# Consider the below code to answer further questions

# Ans-3 No there won't be any difference in the data type of the element present in the both variable 'list' and 'array_list' as long as you specified  'dtype=int' when creating the numpy array . This ensure that the elements in array_list wil be of integer data type , just like the element in list.

# In[1]:


import numpy as np

num_list = [ [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] ]

num_array = np.array(object = num_list)


# In[2]:


num_array


# Q4. Write a code to find the following characteristics of variable, num_array:
# 
# (i)	 shape
# 
# (ii) size

# In[5]:


size=num_array.size


# In[6]:


size


# In[8]:


shape=num_array.shape


# In[9]:


shape


# Q5. Write a code to create numpy array of 3*3 matrix containing zeros only, using a numpy array 
# creation function.

# In[11]:


import numpy as np
m=(3,3)
np.zeros(m)


# Q-6 C
