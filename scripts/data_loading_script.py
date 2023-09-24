#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np


# In[19]:


def load_npy_data(path, files):
    return (np.load(f"{path}/{file}.npy") for file in files)

