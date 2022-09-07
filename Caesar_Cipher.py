#!/usr/bin/env python
# coding: utf-8

# In[2]:


def seizure(key,state):
    symb='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    temp=symb[key:]+symb[:key]
    new_str=''
    x=input('Enter Your String: \n')
    x=x.upper()
    if state == 'e':
        for val in x:
            if val in symb:
                new_str+=temp[ord(val)-65]
            else:
                new_str+=val
    else:
        for val in symb:
            if val!=' ':
                new_str+=symb[temp.index(val)]
            else:
                new_str+=val
    print('The Output is:',new_str)
            
    
while True:
    state=input(r'Encrypt or Decrypt (E/D): '+'\n')
    if state.upper() =='E'or state.upper() =='D':
        key=int(input('Enter The Key (0-25): '))
        if key < 26 and key>0:
            seizure(key,state.lower())
            break
        else:
            print('Invalid Key')
    else:
        print('Invalid Selection')


# In[ ]:




