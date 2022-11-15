#!/usr/bin/env python
# coding: utf-8

# In[1]:


from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {'secure_connect_bundle': 'C:\\Users\\SWETA\\secure-connect-thyroiddata.zip'}
auth_provider = PlainTextAuthProvider('AfrUojylEzrfnACNxTkerjZC', 'bzQJN8CbEzc-23jQh76s67jB0CrR-bEKleGHNdtssPSSvhzCp5OIPYfS1dZ58CWe.hlA-ZPI6lkIKSLYdGSPIfWf,ICTlp_-1X9mzvmZLWE+8o7w8OjqQJ5M6P,8xfmM')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)


# In[2]:


session = cluster.connect('thyroiduserdata')
qry= "create table userinput (age int,sex float,TSH float,TT4 float,T3 float,T4U float,FTI float, diagnosis varchar,primary key(age));"
session.execute(qry)


# In[4]:


rows=session.execute("select * from  userinput;")
for row in rows:
    print(row)


# In[ ]:




