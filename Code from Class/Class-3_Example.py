from pandas import Series, DataFrame
import pandas as pd
import numpy as np

main_dir = "/Users/cuffiewinkler/Desktop/Data/"
git_directory = "/Users/cuffiewinkler/Desktop/GitHub/BigData/"
csv_file_good= "/Class3/Sample_Data_Clean"
csv_file_bad = "/Class3/Sample_Data_Clean"

# OS Module  ----------------------

df = pd.read_csv_csv(os.path.join(main_dir, csv_file_bad))

#Python Data Types -------

#Strings, anything surrounded in quotes

str1 = "hello, computer"
str2 = 'hello,human'
str3 = u'eep'

type(str1) 
type(str2)
type(str3)

#Numeric
int1 = 10
    #integers
float1 = 20.56 
    #decimals
long1 = 999999999999999
    #very long number

#Logical
bool1 = True
    #True of False
notbool1 = 0
    #makes 
bool2 = bool(notbool1)

#Creating lists and Tuples------------
#lists can be changes, tuples cannot; we will almost exclusively use lists
#lists can be appended and extended

list1 = []
list1
list2 [7, 8, a]
list2[2] #output will be a, counting from 0 to the 0,1,2 position
list2[2] = 5 #changes a to 5

#Tuples, can't be changed, denoted by parentheses

tup1 (8, 3, 19)
tup1[2] = 5 #will not change 19 t 5, does not support assignment

# Convert---- take exact element you have a convert
list2 = list(tup1)
tup2 = tuple(list1)

#Appending lists
list2 = [8, 3, 19]
list2.append([3, 90])
len(list2)
list3 = [8, 3, 19]
list3.extend([6, 88]) #8, 3, 19, 6, 88
len(list3)

# Converting lists to series and dataframes

list4 = range[100,105] #ranges (n,m) gives a list from n to m-1

list4 # out: [5, 6, 7, 8, 9]

list5 = range(5) # ranges (N) gives a list from 0 to n-1

list5 # [0, 1, 2, 3, 4]
list6 = ('q', 'r', 's', 't', 'u')

# list to series 3 changes list to series
s1 = series(list4)
s2 = series(list6)

#Create DataFrame from lists or series

List7 = range(60, 65)
zip(list4, list6)
 # puts lists into columns
zip1 = zip(list4, list6, list7)
df1 = DataFrame(zip1)

df2 = DataFrame(zip1, columns = 'two', 'apple', ':)')

df3 = DataFrame(zip1, columns = 2, 'apple', ':)')

df3 = DataFrame(zip1, columns = 2, '2', ':)')
df3[2] # reference column with k (int) 2
df3['2'] #refrence colyumn with key (str) '2'
df3[['2',':)']][3:4] # get column '2'2 and ':)' then get row 3

# make a datafram using dict notation

df4 = DataFram({':(' : List4, 9 ;  List6})



 



   
    


