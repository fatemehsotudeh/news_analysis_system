#!/usr/bin/env python
# coding: utf-8

# In[15]:


import mysql.connector
import sys
sys.path.append('../config/')
from config import DATABASE_CONFIG


# In[16]:


class DatabaseHandler:
    def __init__(self):
        self.conn = mysql.connector.connect(**DATABASE_CONFIG)
        self.cursor = self.conn.cursor()

    def insert_data(self, news_id, title, category, content):
        insert_query = "INSERT INTO news (news_id, title, category, content) VALUES (%s, %s, %s, %s)"
        data = (news_id, title, category, content)
        self.cursor.execute(insert_query, data)
        self.conn.commit()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()


# In[ ]:




