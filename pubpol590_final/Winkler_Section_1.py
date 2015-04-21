from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os


################################################
###### Part a    ########################
################################################

#1. Import and stack (concatenate) the gas consumption data files. 

main_dir = "/Users/louiswinkler/Desktop/GitHub/pubpol590_final/section_1/"

csv1 = 'gas_long_redux_1.csv'
csv2 = 'gas_long_redux_2.csv'
csv3 = 'gas_long_redux_3.csv'
csv4 = 'gas_long_redux_4.csv'
csv5 = 'gas_long_redux_5.csv'

df1 = pd.read_csv(os.path.join(main_dir, csv1))
df2 = pd.read_csv(os.path.join(main_dir, csv2))
df3 = pd.read_csv(os.path.join(main_dir, csv3))
df4 = pd.read_csv(os.path.join(main_dir, csv4))
df5 = pd.read_csv(os.path.join(main_dir, csv5))

df_consump = pd.concat([df1, df2, df3, df4, df5])

#2. Cleaned data

df_consump = df_consump.fillna(0)
#df_consump = df_consump['kwh'][df_consump.kwh < 0] = 0 <----------------------need to fix
df_consump = df_consump.drop_duplicates(['ID', 'date_cer'])

# 3. 

print "\n\n\n" # creates space between prints
print df_consump.shape
print df_consump.kwh.mean()


################################################
###### Part b   ########################
################################################

#1. Import the allocation data and the time correction data 

alloc_file = "residential_allocations.csv"
time_file = "time_correction.csv"

#pull in definitions file
df_def = pd.read_csv(os.path.join(main_dir, alloc_file), usecols=[0,1,],na_values=[''])

#pull in timeseries helper file
df_time = pd.read_csv(os.path.join(main_dir, time_file))
df_time['timecode_cer'] = df_time['day_cer']*100 + df_time['hour_cer']
df_time['datetime'] = pd.to_datetime(df_time['date']) #get the date in datetime, so we can sort later
df_time['monthyear'] = df_time['datetime'].apply(lambda x: datetime(x.year, x.month, 1, 0, 0)) #get just the first day of the month for each date

#2. Merge both data sets to the cleaned dataframe in Part A.

df = pd.merge(df_consump, df_def, df_time)  #<----Need to figure this out










#3.

print "\n\n\n"
print df[df.ID == 1021].head(20)

################################################
###### Part c   ########################
################################################

#1. Aggregate household electricity consumption by month.

grp1 = df.groupby(['Group','ID','year', 'month'])
df=grp1['kwh'].sum().reset_index()


#2. Pivot the monthly consumption data from long to wide.

df_wide = df.pivot('ID', 'kwh_ym', 'kwh')
df_wide.reset_index(inplace = True)
df_wide.columns.name = None


#3. TO RECEIVE CREDIT: 

print "\n\n\n"
print df_piv.shape
print df_piv.head()













