from scipy.stats import ttest_ind
from scipy.special import stdtr
from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os
import time
from datetime import datetime


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

csv_file = "residential_allocations.csv"
time_file = "time_correction.csv"

#pull in definitions file 
df_def = pd.read_csv(os.path.join(main_dir, csv_file), usecols=[0,1],na_values=[''])

#pull in timeseries helper file
df_time = pd.read_csv(os.path.join(main_dir, time_file), parse_dates = [1])
df_time['timecode_cer'] = df_time['day_cer']*100 + df_time['hour_cer']
df_time['datetime'] = pd.to_datetime(df_time['date']) #get the date in datetime, so we can sort later
df_time['monthyear'] = df_time['datetime'].apply(lambda x: datetime(x.year, x.month, 1, 0, 0)) #get just the first day of the month for each date

df_combo = pd.merge(df_consump, df_def)  

df_combo = pd.merge(df_time, df_combo) #<----Need to figure this out

del df_def
del df_time

#3.

print "\n\n\n"
print df_combo[df_combo.ID == 1021].head(20)

#GROUP-----------------------------------------------------------------------------------
###group by day-----------------------------
grp1 = df_combo.groupby(['ResTariff', 'datetime', 'meterid'])

agg1 = grp1['consump'].sum()
agg1 = agg1.reset_index()

grp2 = agg1.groupby(['ResTariff', 'datetime'])

###group by month---------------------------
grp3 = df_combo.groupby(['ResTariff', 'monthyear', 'meterid'])

agg2 = grp3['consump'].sum()
agg2 = agg2.reset_index()

grp4 = agg2.groupby(['ResTariff', 'monthyear'])


#T-TESTS----------------------------------------------------------------------------------

###build dicts of all days and the individual, meter-level sums
trt_day = { k[1]: agg1.consump[v].values for k, v in grp2.groups.iteritems() if k[0]=='A'}
ctrl_day = { k[1]: agg1.consump[v].values for k, v in grp2.groups.iteritems() if k[0]=='E'}
keys_day = trt_day.keys()

###build dicts of all months and the individual, meter-level sums
trt_mth = { k[1]: agg2.consump[v].values for k, v in grp4.groups.iteritems() if k[0]=='A'}
ctrl_mth = { k[1]: agg2.consump[v].values for k, v in grp4.groups.iteritems() if k[0]=='E'}
keys_mth = trt_mth.keys()

#memory management - delete unused variables
del df_combo
del grp1
del grp2
del agg1
del grp3
del grp4
del agg2

#run the t-test for days
tstats_day = DataFrame([(k, np.abs(ttest_ind(trt_day[k], ctrl_day[k], equal_var = False)[0])) for k in keys_day],
                    columns = ['date', 'tstat'])

pvals_day = DataFrame([(k, np.abs(ttest_ind(trt_day[k], ctrl_day[k], equal_var = False)[1])) for k in keys_day],
                    columns = ['date', 'pval'])
                    
#run the t-test for months
tstats_mth = DataFrame([(k, np.abs(ttest_ind(trt_mth[k], ctrl_mth[k], equal_var = False)[0])) for k in keys_mth],
                    columns = ['date', 'tstat'])

pvals_mth = DataFrame([(k, np.abs(ttest_ind(trt_mth[k], ctrl_mth[k], equal_var = False)[1])) for k in keys_mth],
                    columns = ['date', 'pval'])

#mem mgmt
del trt_day               
del ctrl_day
del trt_mth                
del ctrl_mth
                   
#put results into dataframe - nice and neat 
tp_day = pd.merge(tstats_day, pvals_day)
tp_day = tp_day.sort('date')
tp_day = tp_day.reset_index(drop = True)

tp_mth = pd.merge(tstats_mth, pvals_mth)
tp_mth = tp_mth.sort('date')
tp_mth = tp_mth.reset_index(drop = True)


###GRAPHZZZZZZZZZZ###################################
##MONTH GRAPH
fig1 = plt.figure() # initialize plot
ax1 = fig1.add_subplot(2,1,1) # two rows, one column, first plot
ax1.plot(tp_mth['tstat'])
ax1.axhline(2, color='r', linestyle='--')
ax1.axvline(6, color = 'g', linestyle = '--')
ax1.set_title('t-stats over-time (monthly)')

ax2 = fig1.add_subplot(2,1,2) # two rows, one column, first plot
ax2.plot(tp_mth['pval'])
ax2.axhline(0.05, color='r', linestyle='--')
ax2.set_title('p-values over-time (monthly)')
ax2.axvline(6, color = 'g', linestyle = '--')

## DAY GRAPH

fig2 = plt.figure() # initialize plot
ax3 = fig2.add_subplot(2,1,1) # two rows, one column, first plot
ax3.plot(tp_day['tstat'])
ax3.axhline(2, color='r', linestyle='--')
ax3.axvline(171, color = 'g', linestyle = '--')
ax3.set_title('t-stats over-time (daily)')

ax4 = fig2.add_subplot(2,1,2) # two rows, one column, first plot
ax4.plot(tp_day['pval'])
ax4.axhline(0.05, color='r', linestyle='--')
ax4.set_title('p-values over-time (daily)')
ax4.axvline(171, color = 'g', linestyle = '--')


