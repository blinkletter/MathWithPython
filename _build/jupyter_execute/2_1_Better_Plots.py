#!/usr/bin/env python
# coding: utf-8

# # Making Better Plots
# In the ***Making Plots Using Python*** exercise we made a quick plot of an exponential decay function. Here we will demonstrate a few ways to **format** the plot. There are many, many options to try. Just search the web and you will see many examples. We will stick with a **few basic** formatting options that are most helpful.

# ## Your First Plot Again
# **Previously**, we plotted *y = e<sup>–x</sup>*. Below is a repeat of that simple exercise. 
# 
# What is missing? Should we have **labels** for each axis? A **title** perhaps? What other changes would you make?

# In[1]:


import numpy as np                # A library of math functions and data structure
import matplotlib.pyplot as plt   # A library of plotting functions

x = np.linspace(0,5,100)  # make an array of 100 evenly paced values beltween 0 and 5.
y = np.exp(-x)            # make an array of calculated values

plt.plot(x,y)             # plot y vs. x
plt.show()                # show the plot


# ## The Same Thing, Only Better
# We can add elements to the plot such as **titles and labels**. We can set limits on the *x*- and *y*-axis. We can **change the color** of the line. Examine the code below and see how we did all that.
# 
# The **commands** executed below are called "methods".  They are functions built into the `plt` **object**. They modify the object according to the input for the method. When you enter `plt.ylabel("Amount")`, the `plt` object has a **label** added to its *y*-axis. In the last line, the `plt.show()` method **displays and clears** the `plt` object.  Entering `plt.show()` a second time will display nothing unless you build a new plot. 
# 
# There are much **more sophisticated** ways to present plots and we will explore some aspects of this later. However, this is all the **style** that we need to know for now.

# In[2]:


import numpy as np                 # A library of math functions and data structure
import matplotlib.pyplot as plt    # A library of plotting functions

x = np.linspace(0,5,100)           # make an array of 100 evenly paced values beltween 0 and 5.
y = np.exp(-x)                     # make an array of calculated values

plt.plot(x,y, "k--")               # plot y vs. x: the "k" means black, "--" means dashed line

plt.title("Exponential Decay")     # Title of the plot         
plt.xlabel("Time")                 # x-axis label   
plt.ylabel("Amount")               # y-axis label  

plt.xlim([-1,5])                   # set x-axis range
plt.ylim([0,1.2])                  # set y-axis range

plt.show()                         # show the plot


# ## Have Fun
# 
# **Change** some settings above and see what happens. Try plotting a different functions: plot a sine wave; plot a straight line with a slope of $\pi$. **Fool around** with other values and explore. **How** do you get a sine function? **Search** the web for "*NumPy* and sine". How do you get a built-in value for &pi;? Search for *NumPy* and "pi". Are you noticing a pattern here?
# 
# ## Summary
# 
# We have **previously** learned how to make a set of values for an *x*-axis, calculate a corresponding set of values for the *y*-axis and plot the data. Now we have learned **how to add titles and labels** and to **set the color and style** of the line. As we explore more ideas, a new plot setting may be introduced here and there. Keep an eye out for new **opportunities to learn** more about styling plots. 
# 
# 

# In[ ]:




