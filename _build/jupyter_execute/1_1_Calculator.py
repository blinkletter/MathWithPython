#!/usr/bin/env python
# coding: utf-8

# # Basic Math with Python
# We will be using **Python** in this course. The goal is to develop a single tool as a useful resource for interpreting experimental results and solving all sorts of problems. This is not about programming. Will will not be writing programs. We will be issuing **commands** to our loyal computer and making it do all the hard work for us.
# 
# You can **download** the Jupyter notebook for this chapter by using the link at the top.

# ## A calculator
# All of the chapters in this book are **interactive Python notebooks** that have been **converted** to web pages.What you see below is like a printout of the book. Please **download** the original notebook using the link at the top if this page and follow along.
# 
# We can use this interactive Python notebook as a **calculator**. The result of the last command in any code block, such as the one below, will be displayed. We can display the contects of a variable simply by stating it. We can also use a `print()` function to output information. **Explore** the three code blocks below.

# In[1]:


75.35 * 1.15          # calculate the price with tax


# In[2]:


tax = 15                       # percent tax
tip = 20                       # percent tip (when did 20% become the norm?)
dinner_price = 68.85           # values are assigned to variables

dinner_with_tax = dinner_price * (1 + tax/100)   # dinner cost with tax
tip_amount = dinner_price * (tip/100)            # tip calculated on price before tax (as it should be)

total_bill = dinner_with_tax + tip_amount        # calculate the total

total_bill                                       # display the contents of this variable


# In[3]:


total_bill = 126.87
number_of_people = 6                           # we have set the values

per_person = total_bill / number_of_people     # here we do the math
per_person = round(per_person, 2)              # round the result to 2 decimal places

print("The total bill was", total_bill, "dollars")            # output the results
print(number_of_people, "people were splitting the bill")
print("Each person must chip in", per_person, "dollars")      # What each of us must pay (no deadbeats allowed).


# ## Reduce, Reuse and Recycle
# Examine the code blocks above. You could easily **change the values**, the tax rate or the number of people and repeat the calculation quickly. Each of these code blocks is a calculator designed for a purpose. Changing an input will change the result.  You don't need to start from scratch if you want to tip 15% instead of 20%, you just change the one value and execute the code.
# 
# Try changing some values and seeing what happense. Use **\[shift\]\[return\]** to execute the code block.

# ## More Math with NumPy
# Python is a **simple** language. It has built-in functions for the basics but needs help with functions like sine and $e^x$. The NumPy library has many mathematical functions. It is a mainstay of scientific computation. First we will **import** the library as shown below. Then we will use some of the available tools to demonstrate **trigonometry** and to calculate **exponetial growth** of my investment profolio. Examine the code blocks below and see how we use the tools contained inside the NumPy library.
# 
# Observe that we have named the NumPy library that we imported as `np`. This is for convenience (less typing). `np` is now an **object** that contains all the tools of NumPy. To use a function within the library we call it as an extension to the library object. e.g. `np.exp(7)` is a function from NumPy that will give us the exponent of seven or $e^{7}$.

# In[4]:


import numpy as np                # A library of math functions and data structures


# In[5]:


distance_from_tree = 30.0                 # I am standing 30 meters from a tree
angle_to_top_of_tree = 26.0               # I must aim a telecope upwards at this angle to site the top

height = distance_from_tree * np.tan(angle_to_top_of_tree)   # calculate the height
height                                                       # display this value


# In[6]:


P = 10000          # starting ballance
rate = 5           # percent interest. (e.g. 3% per year)
N = 12             # number of payments per time period (e.g. compounded 12 times per year)
t = 10             # number of time periods (e.g. 10 years)

r = rate/100       # true value of interest rate
A = P * (1 + r / N) ** (N * t)  # "**" means "to the power of". (e.g. 10 squared is 10**2)
A = round(A, 2)    # round to dollars and cents

print("An investment of", P, "dollars with ")
print("an interest rate of", rate,"percent per year")
print("compounded",N,"times per year for",t,"years")
print("will result in",A,"dollars")


# ### Notes on the Math 
# From **trigonometry** we know that, in a right triangle, the ratio of the **opposite** side (height of the tree) to the **adjacent** side (distance from tree) is the tangent of the angle between the adjacent side and the **hyponenuse**. Below is that classic formula from high school trigonometry. If we know any two values, we can calculate the third. 
# 
# $$\tan(\theta) = \frac{opposite}{adjacent}$$
# 
# The formula for **compound interest** is given below. Using this, you can plan your retirement (assuming you believe the lies they tell about stock market returns).
# 
# $$ A = P \left(1+ \frac{r}{N} \right)^{N\cdot t} $$
# 
# $A =$ final amount <br>
# $P =$ original principal <br>
# $r =$ interest rate per time period <br>
# $N =$ number or payments per time period <br>
# $t =$ number of time periods
# 
# ### Have Fun
# 
# Change the values in the code block above and **see what happens**. Imagine different angles and distances in your tree measurement. Try comparing compound interest paid monthly with compound interest paid annually over 10 years. How much difference is there? Talk to your banker.

# ## More NumPy Tools
# There is much more to the NumPy library than we will ever use. Below are just a few examples of NumPy that we will use in this course.

# In[7]:


import numpy as np  

radius = 3
print("The value of pi is", np.pi)
print("The area of the circle with a radius of", radius, "is", np.pi*radius**2)
print("The value of e is",np.e)
print("The value of ln(e) is", np.log(np.e))
print("The ln of 10 is",np.log(10))
print("The log of 10 is",np.log10(10))
print("e to the power of 3 is", np.exp(3))
print("The sine of pi radians is", np.sin(np.pi),". It should be zero, shouldn't it?")
print("The cosine of 45 degrees is", np.cos(np.pi/4))   # we must always use radians
print("If the cosine is 0.707, the angle is", np.arccos(.707)/np.pi, "radians")
print("That would be", np.arccos(.707)/np.pi*180,"degrees.")


# ## Tale of the Tape
# One benefit of using an interactive Python notebook is that all your work remains there for you to examine. You will easily be able to **find and correct your error**. Just make the change in the existing code block and execute. Much like the old-fashioned paper tape machines, this calculator keeps a record of your work so you can check later.  
# ## Summary
# We have learned how to perform **math operations** and used a math function from the **NumPy** library. We will see more examples of NumPy tools as we move forward. Don't worry, we won't need very many of them to handle chemistry.

# In[ ]:




