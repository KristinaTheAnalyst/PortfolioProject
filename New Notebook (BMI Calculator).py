#!/usr/bin/env python
# coding: utf-8

# # BMI CALCULATOR
# 

# In[ ]:





# In[29]:


name= input("what is your name?")
weight = int(input("What is your weight in lb?"))
height = int(input("What is your height in in?"))
BMI = (weight*703) / (height*height)
print (BMI)
if BMI > 0:
    if (BMI < 18.5):
        print(name + ", you are underweight")
    elif (BMI < 24.9):
        print (name + ", you have normal weight. Good job")
    elif (BMI < 29.90):
        print (name + ", you are overweight. Little work out will help")
    elif (BMI > 30):
        print (name + ", you are obese")
else:
     print("Invalid inmput")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




