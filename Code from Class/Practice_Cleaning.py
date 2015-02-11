from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os 

main_dir = "/Users/louiswinkler/Desktop/Data/"
git_directory = "/Users/louiswinkler/Desktop/GitHub/BigData/"
csv_file = "sample_missing.csv"

dfmissing = pd.read_csv(os.path.join(main_dir, csv_file))
missing = ['-', ' ', 'NA', '.', 'null']

df_nomissing = pd.read_csv(os.path.join(main_dir, csv_file), na_values = missing)

dataFrame_noDup = dfmissing.drop_duplicates()

consumption = df_nomissing['consump'].isnull()
dfmissing[consumption]

