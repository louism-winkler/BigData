from scipy.stats import ttest_ind
from scipy.special import stdtr
from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os
import time
from datetime import datetime
from dateutil import parser



#IMPORT AND CLEAN DATA----------------------------------------------------------------------------
main_dir = "/Users/louiswinkler/Desktop/data/"
git_directory = "/Users/louiswinkler/Desktop/GitHub/BigData/"
root = main_dir + "class_10/"
df = pd.read_csv(root + "sample_30min.csv", header=0, parse_dates=[1], date_parser=parser.parse)

df_assign = pd.read_csv(root + "sample_assignments.csv", usecols = [0,1])
               
#MERGE
df = pd.merge(df, df_assign)

# add/drop variables
    df['year'] = df['date'].apply(lambda x: x.year)
    df['month'] = df['date'].apply(lambda x: x.month)
    df['day'] = df['date'].apply(lambda x: x.day)
    df['ymd'] = df['date'].apply(lambda x: x.date())

# daily aggregation
grp = df.groupby(['year', 'month', 'day', 'panid', 'assignment'])
grp = df.groupby(['ymd', 'panid', 'assignment'])
    #THESE TWO LINES OF CODE ARE THE SAME, only run 32 or 33
df1 = grp['kwh'].sum().reset_index()


#PIVOTING DATA -- Long to Wide
#1. create column names
#create string names to denote consumption and date
#use ternery expresstion: )true-expr(x) if condition else false-esp(x) for x in list]
#essentially loops through list with an If, Else logical test
#df1[['day_str'] = ['0' + str(v) if v < 10 else str(V) for V in df1['date']] 
## add '0' to <10
#df1[['kwh_ymd'] = 'kwh_'+ df1.year.apply(str) + '_' + df1.day.apply(str) #new string with column containing the data we wants
#

df1['kwh_ymd'] = 'kwh_'+ df1['ymd'].apply(str)

#2. pivot aka long to wide
df1_piv = df1.pivot('panid', 'kwh_ymd', 'kwh')

#clean up
df1_piv.reset_index(inplace=True) #this makes panid its own variable
df1_piv.columns.name = None

#merge time invariant data
df2 = pd.merge(df_assign, df1_piv)

#export data set for regression

df2.to_csv(root + "07_kwh_wide.csv", sep = ",", index=False)






