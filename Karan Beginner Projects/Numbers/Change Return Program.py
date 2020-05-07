#!/usr/bin/env python
# coding: utf-8

# In[18]:


print('Input a value between 0 and 1')
money = float(input())*100
if money > 0 and money < 1000:
    Q = (money // 25)
    money = money - (Q * 25)
    D = (money) // 10
    money = money - (D * 10)
    N = (money - D) // 5
    money = money - (N * 5)
    P = (money-N) // 1
    if P < 0:
        P = 0
   
    print(str(Q) + ' Quarters')
    print(str(D) + ' Dimes')
    print(str(N) + ' Nickels')
    print(str(P) + ' Pennies')


# In[ ]:




