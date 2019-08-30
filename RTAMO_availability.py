# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 15:55:50 2019

@author: Darrell
"""

#%% RTAMO AVAILABILITY MODEL
# 

#%% Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import fsolve

#%% User decisions
A = 0.9 # target availability: proportion of time component can function
L = 0.008 # component failure rate from data base
Tc = 4 / 730 # down time needed for inspection (hours), converted to months
Tr = 48 / 730 # down time needed for repair (hours), converted to months
interval_guess = 12 # inspection interval first guess (months)

#%% Functions
def availability(failure_rate, insp_interval, down_insp, down_repair):
    num = 1 - np.exp(-failure_rate * insp_interval)
    den = failure_rate * (insp_interval + down_insp + down_repair * (num))
    return num / den

#%% Solve Optimal inspection interval numerically

interval_opt = fsolve(lambda x: availability(L, x, Tc, Tr) - A, interval_guess)

#%% Figures
x = np.logspace(0,3,100) # 100 logerly spaced numbers
y = availability(L, x, Tc, Tr) # computing the values of function

# compose plot
plt.semilogx(x,y)
plt.show() # show the plot
plt.xlim([min(x),max(x)])
plt.ylim([0,1])
plt.xlabel('Inspection Interval (months)')
plt.ylabel('Availability')
plt.hlines(A, min(x), max(x), linestyles='-')
plt.vlines(interval_opt, 0, 1, linestyles='--')