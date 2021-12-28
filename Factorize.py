# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 19:50:58 2021

@author: Emad Elshplangy
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Getting the dataset
dataset = pd.read_csv('Wuzzuf_Jobs.csv')


dataset['NEW'] = pd.factorize(dataset['YearsExp'])[0]
a = dataset.iloc[:,[5,-1]]
print(a)