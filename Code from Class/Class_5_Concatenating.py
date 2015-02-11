from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os 

main_dir = "/Users/louiswinkler/Desktop/Data/"
git_directory = "/Users/louiswinkler/Desktop/GitHub/BigData/"
csv1 = "small_data_w_missing_duplicated.csv"
csv2 = "sample_assignments.csv"

##Import Data---------

df1 = pd.read_csv(os.path.join(main_dir, csv1), na_values = ['-', 'NA'])
df2 = pd.read_csv(os.path.join(main_dir, csv2))

#Clean Data-------------------

#Clean df1

df1 = df1.drop_duplicates()
df1 = df1.drop_duplicates(['panid', 'date'], take_last = 'true')

#3 Clean df2

df2[[0,1]]
df2 = df2[[0,1]] #reassigning df2 to a subset

# Copy Dataframes
df3 = df2 #creates a link/reference (alter df2 DOES NOT AFFECT DF3)
df4 = df2.copy() #creating a copy (after df2 does not affect df4)

#replacing data------------------
df2.group.replace(['T', 'C'], [1, 0]) #replaces T and C with 1 and 0 , respectively
                                    #does not change df2
                                    
df2.group = df2.group.replace(['T', 'C'], [1, 0]) # cements replace changes from line 34

#Merging-------------------------
pd.merge(df1, df2) #merges using default "many to one" merge using ther intersection
                   #automatically finds the keys it has in common 
                   
pd.merge(df1, df2, on = ['panid'])     #specifies the key to merge on        
pd.merge(df1, df2, on = ['panid'], how = 'inner')                     
pd.merge(df1, df2, on = ['panid'], how = 'outer')                      
                                    
df5 = pd.merge(df1, df2, on = ['panid'])        

#row binds and column binds ---------------------     
df2
df4

## 3 'row bind'
pd.concat([df2, df4]) # the default is to row bind
pd.concat([df2, df4], axis = 0) # same as above   
pd.concat([df2, df4], axis = 0, ignore_index = True) #ignore_index = Fales is default

# Column bind                    
                                        
pd.concat([df2, df4], axis = 1) 
                   
                   
                   