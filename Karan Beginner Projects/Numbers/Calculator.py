#!/usr/bin/env python
# coding: utf-8

# In[10]:


calc = 'Y'
while calc == 'Y':
    print('enter a number')
    num1 = int(input())
    print('enter another number')
    num2 = int(input())
    print('enter the desired function(+, -, /, or *)')
    function = input()
    if function == '+':
        num3 = num1 + num2
    if function == '-':
        num3 = num1 - num2
    if function == '/':
        num3 = num1 / num2
    if function == '*':
        num3 = num1 * num2
    print(num3)
    print('Continue? Y/N')
    calc = input()
        


# In[ ]:





# In[ ]:




