'''
Q7. Normalize "Age" column using min-max Scaling.

'''

import pandas as pd
import numpy as np

data = {
    "Age" : [18,22,25,30,35]
}


df = pd.DataFrame(data)

min_age = df["Age"].min()
max_age = df["Age"].max()

df["Min_Max_Scale"] = ((df["Age"]-min_age)/(max_age-min_age))

print(df)
