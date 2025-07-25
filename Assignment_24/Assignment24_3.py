'''
Q.3 Group students by gender and calculate average marks.

'''

import pandas as pd

data = {
        'Name' : ["Amit", "Sagar", "Pooja"],
        'Math' : [85,90,78],
        'Science' : [92,88,80],
        'English' : [75,85,82]
        }

df = pd.DataFrame(data)

print(df)


df["Gender"] = ["Male","Male","Female"]


print(df)

Avg_Groupby = df.groupby("Gender")[["Math","Science","English"]].mean()

# Add columns in df
# df["MathAvgGender"] = df.groupby("Gender")["Math"].transform("mean")

print(Avg_Groupby)
print(df)





