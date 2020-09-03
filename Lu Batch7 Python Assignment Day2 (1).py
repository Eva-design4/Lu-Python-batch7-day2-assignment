#!/usr/bin/env python
# coding: utf-8

# In[1]:


# list and its default functions
lst = ["Jane", "Bradley", 23, 34, 89]


# In[2]:


lst


# In[3]:


lst.append("age")


# In[4]:


lst


# In[5]:


lst.count(23)


# In[6]:


lst.pop()


# In[7]:


lst.index(89)


# In[9]:


lst.insert(89,"email")


# In[10]:


lst


# In[11]:


# Dictionary and its default functions
dit = {"name":"Ena","email":"nyars@zim.ke","age":48}


# In[12]:


dit


# In[13]:


dit.keys()


# In[25]:


dit.items()


# In[27]:


dit.get("age")


# In[31]:


dit.clear()


# In[32]:


dit.values()


# In[18]:


# Set and its default functions
st = { "bread", "crumpets", "dounaghts"}


# In[19]:


st


# In[20]:


st.add("jam")


# In[22]:


st


# In[23]:


st.difference()


# In[24]:


st.isdisjoint("bread")


# In[25]:


st.pop()


# In[28]:


st.update("butter")


# In[29]:


st


# In[31]:


st.remove("b")


# In[32]:


st


# In[33]:


# Tuple and explore default methods
tup = ("blackberrys","blueberries","cherrys")


# In[35]:


tup.count("blueberries")


# In[36]:


tup.index("cherrys")


# In[37]:


# Strings and explore default methods
y = ( " The jones family are moving to Australia")


# In[38]:


y


# In[39]:


y.islower()


# In[40]:


y.find("a")


# In[42]:


y.count("s")


# In[43]:


y.isalpha()


# In[44]:


y.upper()


# In[45]:


y.swapcase()


# In[ ]:




