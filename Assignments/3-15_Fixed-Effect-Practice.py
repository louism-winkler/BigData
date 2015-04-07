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
df_assign.rename(columns={'assignment':'T'}, inplace=True)

"""Note: using notation from Allcott 2010"""

#add/Drop varibales-------------
ym = pd.DatetimeIndex(df['date']).to_period('M') # 'M' 

df['ym'] = ym.values
#allows us to quickly link things by year/month

#Monthly Aggregations
grp = df.groupby(['ym', 'panid'])
df = grp['kwh'].sum().reset_index()

#merge static variables
df = pd.merge(df, df_assign)
df.reset_index(drop=True, inplace=True)

# FE Model (Demeaning)
def demean(df, cols, panid):
    """
    inputs: df (pandas dataframe), cols (list of str of column names from df),
                    panid (str of panel ids)
    output: dataframe with values in df[cols] demeaned
    """

    from pandas import DataFrame
    import pandas as pd
    import numpy as np

    cols = [cols] if not isinstance(cols, list) else cols
    panid = [panid] if not isinstance(panid, list) else panid
    avg = df[panid + cols].groupby(panid).aggregate(np.mean).reset_index()
    cols_dm = [v + '_dm' for v in cols]
    avg.columns = panid + cols_dm
    df_dm = pd.merge(df[panid + cols], avg)
    df_dm = DataFrame(df[cols].values - df_dm[cols_dm].values, columns=cols)
    return df_dm

##Set Up variables for demeaning
df['log_kwh'] = df['kwh'].apply(np.log)
df['P'] = 0 + (df['ym'] > 541) #stands for period before and after trials
df['TP'] = df['T']*df['P']

#demean variables
cols = ['log_kwh', 'TP', 'P']
panid = 'panid'
df_dm = demean(df, cols, 'panid')

#Set up regression variables
mu = pd.get_dummies(df['ym'], prefix = 'ym').iloc[:, 1:-1] 
y = df_dm['log_kwh']
X = df_dm[['TP', 'P']]
X = sm.add_constant(X)

## Run Model

fe_model = sm.OLS(y, pd.concat( [X, mu,], axis = 1))
fe_results = fe_model.fit()
print(fe_results.summary())




