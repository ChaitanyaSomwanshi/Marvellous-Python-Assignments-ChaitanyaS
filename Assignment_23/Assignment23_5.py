'''
Q5. Replace 'Pooja' with 'Puja' in the 'Name' column.

'''


import pandas as pd
import numpy as np

data = {
        'Name' : ["Amit", "Sagar", "Pooja"],
        'Math' : [85,90,78],
        'Science' : [92,88,80],
        'English' : [75,85,82]
        }

df = pd.DataFrame(data)

df["Name"] = np.where(df.Name == "Pooja","Puja",df.Name)

# df["Name"] = df["Name"].replace("Puja","Pooja")

print(df)