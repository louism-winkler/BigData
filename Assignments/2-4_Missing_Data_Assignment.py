

#main_dir = "/Users/saurabh/Desktop/Data/"
#git_dir = "/Users/saurabh/Desktop/Github/PubPol590"
#csv_file = "small_data_w_missing_duplicated.csv"


from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os 

main_dir = "/Users/louiswinkler/Desktop/Data/"
git_directory = "/Users/louiswinkler/Desktop/GitHub/BigData/"
csv_file = "small_data_w_missing_duplicated.csv"



## this dataframe has " " and "-" 
dfmissing = pd.read_csv(os.path.join(main_dir, csv_file))

missing = ['-', ' ', 'NA', '.', 'null']

## part 1
## missing data converted to 'NaN' 
dataFrame_noMissing = pd.read_csv(os.path.join(main_dir, csv_file), na_values = missing)

## (part 2
## dataframe with only unique entires
dataFrame_noDup = dfmissing.drop_duplicates()

## part 3
# first find which rows are missing 'consump' data, then extract those rows
consumption = dataFrame_noMissing['consump'].isnull()
dfmissing[consumption]  # simply prints rows that return true in 
                                   # the 'consumption' test.
## part 4
# In other words, search to see if any participant has duplicated dates. 
# Drop the rows where 'consump' is missing for any duplicated values.
dataFrame_noDup = dataFrame_noMissing.drop_duplicates() # no duplicates
df_clean = dataFrame_noDup.dropna()

## part 5
# Take the cleaned data set and find the mean of variable 'consump'
df_clean['consump'].mean()