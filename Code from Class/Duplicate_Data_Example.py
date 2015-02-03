from pandas import Series, DataFrame
import pandas as pd
import numpy as np

#DUPLICATED VALUES---------------------------

## creat new dataframe
zip3 = zip(['red', 'green', 'blue', 'orange']*3, [5, 10, 20, 10]*3,
            [':)', ':D', ':D']*4)