'''
Q5. Add a new column "Status" where student with toatl > = 250 are "Pass", else "Fail".

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