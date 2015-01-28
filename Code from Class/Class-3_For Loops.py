from pandas import Series, DataFrame
import pandas as pd
import numpy as np

main_dir = "/Users/cuffiewinkler/Desktop/Data/"
git_directory = "/Users/cuffiewinkler/Desktop/GitHub/BigData/"
csv_file_good= "/Class3/sample_data_unclean"

#For Loops------------------

df = pd.read_csv(os.path.join(main_dir, csv_file))
df1 = read_csv([1, 2, 3,])

list1 = range(10,15)
list2 = ['a', 'b', 'c']
list3 = [1, 'a', True]

# iterating over elements (for loops)
for v in list1:  # for "value" "chosen list":
    v

for v in list1:  
    print(v)

for v in list2:  
    print(v)    
                
for v in list3:  
    print(v, type(v))     
 