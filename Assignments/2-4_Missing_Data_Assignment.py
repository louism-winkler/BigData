from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os 

main_dir = "/Users/louiswinkler/Desktop/Data/"
git_directory = "/Users/louiswinkler/Desktop/GitHub/BigData/"
csv_file = "small_data_w_missing_duplicated.csv"


dfmissing = pd.read_csv(os.path.join(main_dir, csv_file)) #contains '-', ' '

missing = ['-', ' ', 'NA', '.', 'null'] #missing is now considered a list

#convert missing data converted to 'NaN' 
df_nomissing = pd.read_csv(os.path.join(main_dir, csv_file), na_values = missing)

# dataframe with only unique entires
dataFrame_noDup = dfmissing.drop_duplicates()

#find which rows are missing 'consump' data, then extract those rows
consumption = df_nomissing['consump'].isnull()
dfmissing[consumption]  # returns rows that are true in the 'consumption' test.

#search for duplicated dates; Drop the rows where 'consump' is 
#missing for any duplicated values.
dataFrame_noDup = df_nomissing.drop_duplicates() # no duplicates
df_clean = dataFrame_noDup.dropna()

# Takes cleaned data set and finds the mean of variable 'consump'
df_clean['consump'].mean()