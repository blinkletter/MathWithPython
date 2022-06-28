#!/usr/bin/env python
# coding: utf-8

# # Making Plots Using *Python*
# You can demonstrate the results of math functions using ***Python***. You can read in (or type in) data and plot the data. You can fit the data to a function and obtain the parameters and statistical information. Everything that **Excel** can do, *Python* can do for free.

# ## Import Your Tools
# *Python* is a simple language and we might write hundreds of lines of code to do everything that this exercise needs. However others have done this already. We will import "**packages**" that contain functions for everything we want to do. We will call these functions as we proceed. Below are the tools we need and the commands to import them.
# 
# We have seen some tools from NumPy. Here we will introduce tools for plotting from ***MatPlotLib***. We will use a subsection of *MatPlotLib* called ***PyPlot***. It is best for simple plots. We will import the *PyPlot* tools into an object called `plt`. 

# In[1]:


import numpy as np                # A library of math functions and data structure
import matplotlib.pyplot as plt   # A library of plotting functions


# ## Your First Plot
# For a quick first example we will **plot** an exponential decay curve. We will plot *y = e<sup>–x</sup>*. First we need a ***x*-axis**. As you see below, we will use the `linspace` tool from *NumPy* to create an evenly spaced array of values between two points. We will then calculate a new array for the ***y*-axis** by applying the exponential decay function.  We now have a set of x,y values to plot.
# 
# We will then **plot the *x,y* data** using tools from the `plt` object Now we will have our first plot.

# In[2]:


x = np.linspace(0,5,100)  # make an array of 100 evenly paced values beltween 0 and 5.
y = np.exp(-x)            # make an array of calculated values

plt.plot(x,y)             # plot y vs. x
plt.show()                # show the plot


# ## Your Next Plot
# Let us **demonstrate** first order **reaction kinetics**. We will plot the concentration of reactant and product for the reaction *A &rarr; B*. We know that the instantaneous rate at any given time point is&hellip;
# 
# $$-\frac{\partial [A]}{\partial t}=\frac{\partial [B]}{\partial t}=k[A] $$ 
# 
# &hellip;and the integrated rate equation that describes the concentrations of *A* and *B* as they change over time are 
# 
# $$ [A]_t=[A]_0 e^{-k t}  \text{ and }  [B]_t=[A]_0 \left( 1-e^{-k t} \right)$$ 
# 
# Below we will create an array of values for the *x*-axis and then make two calculated arrays for the *y*-axis. One set is for [*A*] and the other is for [*B*]. We will then plot them.

# In[3]:


A0 = 1.5                  # create a variable that represents the initial concentration
k = 0.34                  # a variable that represents the rate constant

t = np.linspace(0,5,100)  # make an array of 100 evenly paced values beltween 0 and 5 for time
yA = A0*np.exp(-k*t)      # make an array of calculated values for [A]
yB = A0*(1-np.exp(-k*t))  # make an array of calculated values for [B]

plt.plot(x,yA)            # plot y vs. x
plt.plot(x,yB)            # plot y vs. x

plt.show()                # show the plot


# ## Have Fun
# **Change** the value for *k* (rate constant) in the code block above and see what happens. Plot a different function (e.g. n<sup>x</sup> - 3.) **Fool around** with other values and explore. Undo is your friend. Idleness is your enemy.
# 
# ## Summary
# We have learned how to **make a set of values** for an *x*-axis, **calculate a corresponding set of values** for the *y*-axis and **plot** the data. We have seen that repeated plot commands will add to the plot until a `plt.show()` function is called to display the results. 
# 
# There are many, many **options and features** to the *MatPlotLib* plotting system. We can change the style and format, we can have multiple plots in a single figure, we can save the plots in a variety of formats and so much more. The *NumPy* tools and other toolsets that we import will provide many useful functions for math and interpreting data. We will learn as we go.

# In[ ]:




