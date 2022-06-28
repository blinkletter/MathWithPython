#!/usr/bin/env python
# coding: utf-8

# # The ICE Table in *Python*
# 
# We often can determine the **final concentrations** of a system using the initial concentrations and the equilibrium constant, *K<sub>eq</sub>*. You will be familiar with the **ICE table** method, which helps us to set up the equations. Let us use the example of a weak acid.
# 
# ## Weak Acid Equilibrium
# 
# When we **add** 0.1&nbsp;*g* of acetic acid to 100&nbsp;*mL* of pure water, what is the resulting *pH*? We can **solve** this problem with a pad of paper and a calculator or we can build a notebook that can be reused again and again. Consider the code below.

# ### Start With the Facts
# First we define some **variables** and constants. If we want to reuse this notebook for another monoprotic **weak acid**, we could do so by changing only this section.

# In[1]:


molar_mass_of_acid = 60.05 # in g/mol
pKa = 4.75                 

acid_mass = 1.1            # in g
water_volume = 100         # in mL

Ka = 10**(-pKa)

moles = acid_mass / molar_mass_of_acid    # moles of acid
volume = water_volume / 1000              # litres of water

initial_conc = moles / volume

print("Initial concentration of acid:")
print(round(initial_conc,5), "moles/L")

print("The Ka of the acid:")
print(round(Ka,7))


# ### Set Up the Equation
# We know the **equilibrium** expression for the acid dissociation...
# 
# $$AcOH \rightleftharpoons AcO^- + H^+$$  
# $$K_a = \frac{[AcO^-][H^+]}{[AcOH]}$$
# 
# The **initial** concentrations of acetic acid and the products could be described as...
# 
# $$[AcOH]_0 = some value$$
# $$[AcO^-]\:and\:[H^+] = 0$$
# 
# The **change** in the concentrations as the reaction moves forward is represented by the symbol *x*. We can say that the new concentrations will be...
# 
# $$[AcOH]_{eq} = some value-x$$
# $$[AcO^-]_{eq}\:and\:[H^+]_{eq} = x$$
# 
# Therefore the **equilibrium** will occure when the concentrations amount to the value of the equilibrium constant.
# 
# $$K_a = \frac{[AcO^-]_{eq}[H^+]_{eq}}{[AcOH]_{eq}}$$
# 
# and so...
# 
# $$K_a = \frac{x \cdot x}{some value-x}$$
# 
# ### Using SymPy
# 
# We need to solve for *x*. *SymPy* will do all the hard work.

# In[2]:


import sympy

x = sympy.symbols("x")

expr = x*x/(initial_conc-x) - Ka
display(expr)


# In[3]:


solution_list = sympy.solvers.solve(expr, x)  
print(solution_list)


# ### Pick a Number
# **Inspect** the solution. There are **two possibilities**. However it is impossible for the concentration of product to be negative in value. So we will choose the only possible answer.

# In[4]:


change = solution_list[1]
print(change)    


# ### Produce the Result
# We can now **report** the results. 

# In[5]:


import math

print("The initial concentration of acid is", initial_conc) 
print("-"*20)
print("At equilibrium we will have the following concentrations")
print("[Acid] =", initial_conc - change)
print("[hydronium] =", change)
print("[Conj. base] =", change)
print("-"*20)

pH = -math.log10(change)
print("pH =", pH)


# ### Styling Printouts of Numbers
# 
# You can decide how many **significant figures** to use when you write down the result above. But you can build it right into your print commands using the `.format()` method for *Python* text strings. Consider the following code. The \{:.3\} is the placeholder in the string where the format method will place a **formatted** number, the ":" indicates that the number should not be padded with zeros and the ".4" means 4 decimal places.

# In[6]:


import math

print("The initial concentration of acid is {:.4} M".format(initial_conc))    # 4 sig figs
print("-"*20)
print("At equilibrium we will have the following concentrations")
print("[Acid] = {:.3f} M".format(initial_conc - change))   # floating point with 3 decimal places
print("[hydronium] = {:.3e} M".format(change))             # exponential format with 3 decimal places
print("[Conj. base] = {:.3} M".format(change))
print("-"*20)

pH = -math.log10(change)
print("pH = {:.3}".format(pH))


# In[7]:


import sympy

x = sympy.symbols("x")

expr = x*x/(initial_conc-x) - Ka
display(expr)


# ## Summary
# We can now **calculate** the *pH* of a solution of a weak acid given an amount of acid, the volume and the *pK<sub>a</sub>* value for the weak acid. We can **change** the values in the first block and then execute the notebook code to get to the final answer. We will never need to do math again (except on the test and final exam, so don't get too lazy).
