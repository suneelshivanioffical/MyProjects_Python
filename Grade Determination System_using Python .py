
# coding: utf-8

# # _Grade Determination System_using Python

# In[2]:


#_Develop a program that determines a student's grade based on their test score. The program should:
    #_• Ask the user to enter a score.
    #_• Use selection structures (if, if-else, switch-case) to determine the grade based on the score ranges (A, B, C, D, F).
    #_• Output the corresponding grade.

score = int(input("Enter your Score : "))

if score >= 90 :
   print("Grade : A")
elif score >= 80:
   print("Grade : B")
elif score >= 70:
   print("Grade : C")
elif score >= 60:
   print("Grade : D")

else:
    print("Grade : F")

