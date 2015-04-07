from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os 

main_dir = "/Users/louiswinkler/Desktop/Data"
git_directory = "/Users/louiswinkler/Desktop/GitHub/BigData/"
root = main_dir + "/class_6"

#pathing_______________________________

paths = [os.path.join(root,v) for v in os.listdir(root) if v.startswith("file_")]

df = pd.concat([pd.read_csv(v, names = ['panid', 'date', 'kwh']) for v in paths], ignore_index = True)

df_assign = pd.read_csv(root + "/sample_assignments.csv", usecols = [0,1])

#merge
df = pd.merge(df, df_assign)

#groupby aka "split, apply, combine"

#split by C/T, pooled w/o time
groups1 = df.groupby(['assignment']) #splitting by assignment
groups1.group

#apply to mean
groups1['kwh'].apply(np.mean) #.apply is to 'apply' any type of function
groups1['kwh'].mean() #is an intenral method (faster)

%timeit -n 100 groups1['kwh'].apply(np.mean) #.apply is to 'apply' any type of function
%timeit -n 100 groups1['kwh'].mean() #is an intenral method (faster)

#split by C/T, pooled w/o time
groups2 = df.groupby(['assignment', 'date']) #splitting by assignment
groups2.group

#apply to mean
groups2['kwh'].mean() #is an intenral method (faster)

groups2 = df.groupby(['date', 'assignment']) #splitting by assignment
groups2.group

#unstack-------------------------

gp_mean = groups2['kwh'].mean()
gp_unstack = gp_mean.unstack('assignment')

gp_unstack['T'] #means over time of all treated panids

