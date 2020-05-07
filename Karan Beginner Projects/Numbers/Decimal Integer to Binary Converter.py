#!/usr/bin/env python
# coding: utf-8

# In[27]:


def bintodecint(num):
    decall = []
    if num % 2 == 0:
        firstdec = 0
    else:
        firstdec = 1
    decall.append(firstdec)
        
    while num != 1:
        num = num // 2
        if num % 2 == 0:
            dec = 0
        else:
            dec = 1
        decall.append(dec)
    decall.reverse()
    decall = list(map(str, decall))
    number = ''.join(decall)
    print(number)
num = int(input())
bintodecint(num)


# In[ ]:




