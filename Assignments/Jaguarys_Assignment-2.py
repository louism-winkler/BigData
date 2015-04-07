from scipy.stats import ttest_ind
from scipy.special import stdtr
from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

#IMPORT AND CLEAN CER DATA

main_dir = "/Users/louiswinkler/Desktop/data/"
git_directory = "/Users/louiswinkler/Desktop/GitHub/BigData/"
csv_file = "cer_data/SME and Residential allocations.csv"
root = main_dir + "cer_data/"

# PATHING --------------
paths = [os.path.join(root,v) for v in os.listdir(root) if v.startswith("File")]

# IMPORT AND STACK ---------
df = pd.concat([pd.read_csv(v, names = ['panid', 'date', 'kwh']) for v in paths],
ignore_index = True)
df_assign = pd.read_csv(root + "SME and Residential allocations.csv", usecols = [0,1])

#build file list
all_files = [os.path.join(main_dir, v) for v in os.listdir(main_dir) if v.startswith("File")]
