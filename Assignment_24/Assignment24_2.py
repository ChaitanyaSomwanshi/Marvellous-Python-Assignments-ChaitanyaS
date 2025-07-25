'''
Q2. Create a gender column and perform one-hot encoding

'''

import pandas as pd

data = {
        'Name' : ["Amit", "Sagar", "Pooja"],
        'Math' : [85,90,78],
        'Science' : [92,88,80],
        'English' : [75,85,82]
        }

df = pd.DataFrame(data)

df["Gender"] = ["Male","Male","Female"]

print(df)

print(pd.get_dummies(df["Gender"]))



