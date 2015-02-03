from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os 

main_dir = "/Users/louiswinkler/Desktop/Data/"
git_directory = "/Users/louiswinkler/Desktop/GitHub/BigData/"
csv_file = "sample_missing.csv"

#Importing Data: Setting missing values (sentinels)

df = pd.read_csv(os.path.join(main_dir, csv_file))
df.head() # top 5 values
df.head(10) # head (n) gives top n rows
df(:10) # this is slicing, same as df.head
df.tail(10) #tail(n) gives bottom n rows 

df['consump'].head(10).apply(type) #apply function 'type' to top 10 rows of consum

# we don't want string data. periods '.' are common place holders for missing data
# in some programing langauges (stata). So we need to create new sentinels to adjust for this. 
# missing value sentiels to adjust. use na_values to use sentinels.

missing = ['.', 'NA', 'NULL', ''] #missing is now considered a list
df = pd.read_csv(os.path.join(main_dir, csv_file), na_values = missing)
# allows us to deinfe what text is considered a missing value. We could use numbers, or whatever we want. 
df.head(10) #NaN = not a number
df['consump'].head(10).apply(type)


#mising data (using smallter dataframe) ---------------------------------

# quick top, you can repeast lists by multiplying

[1, 2, 3]
[1, 2, 3]*3

# types of missing data
None
np.nan
type(None)
type(np.nan) # want to use this version when working with missing data

#create a small sample data set

zip1 = zip([2,4,8], [np.nan, 5, 7], [np.nan, np.nan, 22])
df1 = DataFrame(zip1, columns = ['a', 'b', 'c'])

## search for missing data using 
df1.isnull() #pandas method to find missing data

# any object plus . and then tab will display 

np.isnan(df1) #numpy way

#subset of columns 
cols = ['a', 'c']
df1[cols]
df1[cols].isnull()

# for series
df1['b'].isnull()

## find non-missing values
df1.notnull()
df1.isnull()

df1.notnull() == df1.isnull()

# -->Filling in or dropping vlaues

#pandas method 'fillna'

df1.fillna(999)
df2 = df1.fillna(999)

# Pandas methond: 'dropna' Note: Python uses Null, na, NaN as interchangeable

df1.dropna() # by default, this drops ROWS with ANY missing values, often too strict
df1.dropna(axis = 0, how = 'any') # drops ROWS with ANY missing values

# 2 axis, 0 is a row, 1 is a column

df1.dropna(axis = 1, how = 'any') # drops COLUMNS with ANY missing values

df1.dropna(axis = 0, how = 'all') # drops ROWS with ALL missing values 

# try it out odject df

df.dropna(how = "all") #prob need for homework

#seeing rows with missind data----------------

df3 = df.dropna(how = 'all')
df3.isnull()
df3['consump'].isnull()
rows = df3['consump'].isnull()
df3[rows]



















