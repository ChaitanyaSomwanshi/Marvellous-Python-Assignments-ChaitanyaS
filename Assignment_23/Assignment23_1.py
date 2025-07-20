'''
Q1. Create a DataFrame for student marks and print basic information like shape, columns, and data types.

data = {
        'Name' : ["Amit", "Sagar", "Pooja"],
        'Math' : [85,90,78],
        'Science' : [92,88,80],
        'English' : [75,85,82]
        }

Note : Consider the same dataset for this as well as next assignment.


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
print("Sample dataset is :")
print(Line)
print(df)
print(Line)

print("Shape of data set is ", df.shape)
print(Line)
print("Columns in dataset are :", df.columns)
print(Line)
print("Datatype of columns are :", df.dtypes)
print(Line)




