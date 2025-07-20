'''
Q2. Use the DataFrame from Q1 and print descriptive statistics using .describe().

'''

import pandas as pd

data = {
        'Name' : ["Amit", "Sagar", "Pooja"],
        'Math' : [85,90,78],
        'Science' : [92,88,80],
        'English' : [75,85,82]
        }

df = pd.DataFrame(data)

Line = "_"*58

print(Line)
print("Summary of dataset :" )
print(Line)
print(df.describe())
print(Line)