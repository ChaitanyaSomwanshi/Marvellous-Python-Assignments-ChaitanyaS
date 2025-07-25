'''
Q8. Fill missing values in a numeric column using interpolation.

'''

import pandas as pd
import numpy as np

data = {"Marks" : [85,np.nan,90,np.nan,95]}


df = pd.DataFrame(data)

df["Marks"] = df["Marks"].interpolate(method="linear")

print(df)