# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 14:40:02 2019

@author: Darrell
"""

#%% RTAMO RELIABILITY MODEL
# 

#%% Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import fsolve

#%% User decisions
R = 0.9 # target reliability: prob. component won't fail over any given month
L = 0.0063 # component failure rate from data base
interval_guess = 12 # inspection interval first guess (months)

#%% Functions

reliability = lambda failure_rate, inspection_interval : -((failure_rate * inspection_interval)**-1)*(np.exp(-failure_rate * inspection_interval) - 1)

#%% Solve Optimal inspection interval numerically

interval_opt = fsolve(lambda x: reliability(L, x) - R, interval_guess)