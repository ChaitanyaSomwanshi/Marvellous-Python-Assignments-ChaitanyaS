'''
Q7. Export the final DataFrame to a CSV file.

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

df["Total"] = df["Math"] + df["Science"] + df["English"]

df["Status"] = np.where(df["Total"] > 250, "Pass", "Fail")

print(df)

df.to_csv("StudentMarks.csv", index = False)