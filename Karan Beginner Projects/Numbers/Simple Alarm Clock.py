#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pyinputplus, time, winsound
print('Enter the emount of time til you would like to be notified(minutes)')
minutes = pyinputplus.inputInt()
time.sleep(60*minutes)
for _ in range(15):
    winsound.Beep(600, 500)


# In[ ]:





# In[ ]:




