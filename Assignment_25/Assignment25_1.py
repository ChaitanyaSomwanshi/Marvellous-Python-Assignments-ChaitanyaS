'''
Q1. Detect outliers in the "Salary" column using the IQR method.

'''

import pandas as pd




data = {
        "Salary" :[25000,27000,29000,31000,50000,100000]
        }

df = pd.DataFrame(data)


Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)

IQR = Q3 - Q1

print("IQR :", IQR)