'''
Q1. Normalize the 'Math' score using Min-Max scaling.

'''

import pandas as pd

data = {
        'Name' : ["Amit", "Sagar", "Pooja"],
        'Math' : [85,90,78],
        'Science' : [92,88,80],
        'English' : [75,85,82]
        }

df = pd.DataFrame(data)

math_min = df["Math"].min()
math_max = df['Math'].max()


print(math_min)
print(math_max)

df['Math_NM'] = (df['Math']-math_min)/(math_max-math_min)

print(df)