#!/usr/bin/env python
# coding: utf-8

# # *Pandas* and Plotting Data
# We have seen how to plot a function by generating a list of numbers for an *x*-axis and calculation a resulting *y*-axis from that list. Now let us consider plotting **experimental data**.
# 
# There are two ways to generate a set of *x*,*y* data in *Python*. We can **type it in** or we can **read it in** from a file. In this exercise we will demonstrate both. How should this data be represented? Previously, we used **two corresponding lists**. One list for the *x* values and another for the *y* values. Here we will begin using the ***Pandas*** library. It contains the tools for building a data structure called a **dataframe**. Dataframes are just a set of values arranged in columns and rows.
# 
# ## The Tools
# As always, we must begin by importing the tools that we will be using.

# In[1]:


import numpy as np                # A library of math functions and data structure
import pandas as pd               # Contains the dataframe object and related methods
import matplotlib.pyplot as plt   # A library of plotting functions


# ## Your Data
# 
# Consider the code block below. We are going to create a set of *x,y* data as **two lists** and then read in another set of *x,y* data using *Pandas*.  ***Pandas*** provides the tool we will be using to **import the data**. We wont have to write a small program to read a text file - *Pandas* will do that for us. We are not computer programmers, we are computer users and we will be standing by that philosophy.
# 
# **Note**: You can download this notebook using the link above but the **datafile.csv** file won't come with it. You can obtain the data file from the resources on the **moodle site**.

# In[2]:


print("Here is my experimental data as two lists")
x = [0,4,6,10,15,18]           # A list of 6 numbers
y = [0,2.5,2.8,5.6,7.9,8.2 ]   # Another list of 6 numbers. Do they correlate to the first list?
print("x values:",x)
print("y-values:",y)
print()
                               # Read a data file. It should be in the same directory as this notebook
print("Here is data read in from a data file as a data frame object")
xydata = pd.read_csv("datafile.csv")
display(xydata)                # Display is like print but uses the graphical features of this notebook


# ## Plot The Data
# 
# We have two sets of data. One set is a **pair of lists** for *x* and *y* and the other is a **dataframe object**. We can plot the lists as previously demonstrated. *MatPlotLib* is designed to use two lists for the data. It predates the *Pandas* library and knows nothing of dataframes. We can address each column in a dataframe by using its heading and feed any two columns in a dataframe to *MatPlotLib* that way. **Examine** the code blocks below and **compare** the two approaches.

# In[3]:


plt.plot(x,y, "ko-")                       # "k" = black, "-" = solid line, "o" = circles for data points

plt.title("Plotting a Pair of Lists")      # Title of the plot         
plt.xlabel("List of x data")               # x-axis label   
plt.ylabel("List of y data")               # y-axis label  
print("Here is a plot of the data that was typed in as a pair of lists")
plt.show()                                 # show the plot


# In[4]:


plt.plot(xydata["Time"], xydata["Volts"], "b^-.") # "b" = blue, "-." = dash-dot line, "^" = triangles for data points

plt.title("Plotting a Pair of Columns")           # Title of the plot         
plt.xlabel("Column of x data")                    # x-axis label   
plt.ylabel("Column of y data")                    # y-axis label  
print("Here is a plot of two columns of data from the dataframe")
plt.show()                                        # show the plot


# ## Don't Connect the Dots
# The plots above are "**spaghetti plots**". The data points are connected by a line. This is a common way to plot statistical data but it is **not favoured** in chemistry. Lines should represent the **model** to which we are fitting the experimental data. For now let us demonstrate a "**scatter plot**", a plot with data points only.

# In[5]:


plt.plot(xydata["Time"], xydata["Volts"], "kx") # "k" = black, "x" = cross for data points

plt.title("Plotting a Pair of Columns")           # Title of the plot         
plt.xlabel("Column of x data")                    # x-axis label   
plt.ylabel("Column of y data")                    # y-axis label  
print("Just the points. What function would you model this with?")

plt.ylim([0,0.7])
plt.show()                                        # show the plot


# ## Summary
# Now we can use **experimental data** in our plots. How can we interpret this data? **Next** we will explore fitting a proposed model to the data. Does our model fit? If so, we may be on the right track, if not then we may need to change the model.
# 
# ## Resources
# The **datafile.csv** data file can be obtained from the resources section of the course **moodle site**. The contents of the file are displayed below so that you can **make it yourself** if you are unable to access moodle.
# 
# **datafile.csv**
# ```
# Time,Volts
# 1.0,0.11
# 3.0,0.25
# 5.0,0.34
# 10.0,0.45
# 20.0,0.58
# 50.0,0.61
# ```

# In[ ]:




