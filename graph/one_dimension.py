
# coding: utf-8

# In[1]:

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[2]:

np.random.seed(1000)
y = np.random.standard_normal(20)


# In[7]:

x = range(len(y))
#plt.plot(x, y)
plt.plot(y)


# In[8]:

plt.plot(y.cumsum())
plt.grid(True)
plt.axis('tight')


# In[9]:

plt.plot(y.cumsum())
plt.grid(True)
plt.xlim(-1,20)
plt.ylim(np.min(y.cumsum()) - 1, np.max(y.cumsum()) + 1)


# In[10]:

plt.figure(figsize=(7, 4))
# the figsize parameter defines the size of the figure in(width, height)
plt.plot(y.cumsum(), 'b', lw=1.5)
plt.plot(y.cumsum(), 'ro')
plt.grid(True)
plt.axis('tight')
plt.xlabel('index')
plt.ylabel('value')
plt.title('A Simple Plot')


# In[ ]:



