
# coding: utf-8

# In[1]:

import os, time 

path_to_watch = "E:\\Balaji\\Visa docs\\Source"

before = dict ([(f, None) for f in os.listdir (path_to_watch)])
print (before)


# In[2]:

if True:
    time.sleep (30)
    after = dict ([(f, None) for f in os.listdir (path_to_watch)])
    added = [f for f in after if not f in before]
    removed = [f for f in before if not f in after]
    if added: 
        print ("File added")
        print ("Added: " .join(added))
        import AWSRekog_DriverAuth      
    elif removed:
        print ("File removed")
        print ("Removed: " .join(removed)) 
    else:
        print ('No changes in files')
        import AWSRekog_DriverAuth      


# In[ ]:



