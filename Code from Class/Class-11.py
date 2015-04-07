from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import statsmodels.api as sm
import os
from dateutil import parser # use this to ensure dates are parsed correctly

main_dir = "/Users/louiswinkler/Desktop/data/"
root = main_dir + "/data/"
paths = [root + v for v in os.listdir(root) if v.startswith("08_")]

# import data --------------
df = pd.read_csv(paths[1], header=0, parse_dates=[1], date_parser=np.datetime64)
df_assign = pd.read_csv(paths[0], header = 0)

# add/drop variables ------
df['year'] = df['date'].apply(lambda x: x.year)
df['month'] = df['date'].apply(lambda x: x.month)

# Monthly aggregation----------------
grp = df.groupby(['year', 'month', 'panid'])
df = grp['kwh'].sum().reset_index()

# PIVOT DATA ---------------
# go from 'long' to 'wide'

df['mo_str'] = ['0' + str(v) if v < 10 else str(v) for v in df['month']]  #add '0' to < 10
df['kwh_ym'] = 'kwh_' + df.year.apply(str) + '_' + df.mo_str.apply(str)

df_piv = df.pivot('panid', 'kwh_ym', 'kwh')
df_piv.reset_index(inplace = True)
df_piv.columns.name = None #converted over time data to cross-sectional values

#merge the static values (e.g. assignments)
df = pd.merge(df_assign, df_piv)
#del df_piv, df_assign

# GENERATE DUMMIES FROM QUALITITATIVE (I.E. CATEGORIES)
df1 = pd.get_dummies(df, columns = ['gender'])
df1.drop(['gender_M'] axis = 1, inplace=True)








## 1. create column names for wide data
# create strings names and denote consumption and date
# use ternery expression: [true-expr(x) if condition else false-exp(x) for x in list]
#df1['day_str'] = ['0' + str(v) if v < 10 else str(v) for v in df1['date']] # add '0' to < 10
#df1['kwh_ymd'] = 'kwh_' + df1.year.apply(str) + '_' + df1.month.apply(str) + 
#            '_' + df1.day_str.apply(str)

df1['kwh_ymd'] = 'kwh_' + df1['ymd'].apply(str)

# 2. pivot! aka long to wide
df1_piv = df1.pivot('panid', 'kwh_ymd', 'kwh')

# clean up for making things pretty
df1_piv.reset_index(inplace=True) # this makes panid its own variable
df1_piv
df1_piv.columns.name = None
df1_piv

# MERGE TIME invariant data ----
df2 = pd.merge(df_assign, df1_piv) # this attachin order looks better
