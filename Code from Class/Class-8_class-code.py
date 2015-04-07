from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

main_dir = "/Users/louiswinkler/Desktop/data/"
git_directory = "/Users/louiswinkler/Desktop/GitHub/BigData/"
root = main_dir + "class_8/"

# PATHING --------------
paths = [os.path.join(root,v) for v in os.listdir(root) if v.startswith("file_")]

# IMPORT AND STACK ---------
df = pd.concat([pd.read_csv(v, names = ['panid', 'date', 'kwh']) for v in paths],
    ignore_index = True)
    
df_assign = pd.read_csv(root + "sample_assignments.csv", usecols = [0,1])


# MERGE ---------
df = pd.merge(df, df_assign)

# split by C/T, pooled w/o time
groups1 = df.groupby(['assignment']) # splitting by assignment
groups1.groups

# split by C/T, pooling w time
groups2 = df.groupby(['date','assignment']) # splitting by assignment

# apply the mean
groups2['kwh'].mean() # .mean() is an internal method (faster)

grp = df.groupby(['assignment', 'date'])

trt = {k[1]: df.kwh[v].values for k, v in grp.groups.iteritems() if k[0] == 'T'}
ctrl = {k[1]: df.kwh[v].values for k, v in grp.groups.iteritems() if k[0] == 'C'} 
keys = trt.keys()

tstats = DataFrame([(k, np.abs(ttest_ind(trt[k], ctrl[K], equal_var=False)[0])) for k in keys], columns = ['date', 'tstat'])

