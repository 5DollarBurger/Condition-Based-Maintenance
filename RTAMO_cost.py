# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 15:30:58 2019

@author: Darrell
"""

#%% RTAMO COST MODULE
# 

#%% Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import fsolve

#%% User decisions
c1 = 2300 # cost of inspection
c2 = 500000 #347200 # cost of failure
L = 0.004761905 # component failure rate from data base
gamma = 0.633066211589233
interval_guess = 12 # inspection interval first guess (months)

#%% Functions
CR_insp = lambda cost_insp, insp_int : cost_insp / insp_int # cost rate of inspection

def CR_fail(failure_rate, cost_fail, delay_rate, insp_int): # cost rate of failure
    Pd = (1 - np.exp(-delay_rate * insp_int)) / (delay_rate * insp_int)
    D = failure_rate * cost_fail * (1 - Pd)
    return D

#%% Solve Optimal inspection interval numerically



#%% Figures
x = np.logspace(0,3,1000) # 100 logerly spaced numbers
cost1 = CR_insp(c1, x)
cost2 = CR_fail(L, c2, gamma, x)
cost3 = cost1 + cost2

# compose plot
plt.semilogx(x, cost1, label='Inspection cost')
plt.semilogx(x, cost2, label='Failure cost')
plt.semilogx(x, cost3, label='Total cost')
plt.show() # show the plot
plt.xlim([min(x),max(x)])
#plt.ylim([0,1])
plt.xlabel('Inspection Interval (months)')
plt.ylabel('Cost Rate ($/month)')
plt.legend()
plt.hlines(min(cost3), min(x), max(x), linestyles='-')
#plt.vlines(x[np.argmin(cost3)], 0, min(cost3), linestyles='--')
plt.axvline(x[np.argmin(cost3)], linestyle='--', color = 'k')

print('You should inspect every ', x[np.argmin(cost3)], 'months')
print('It will cost you $', min(cost3))