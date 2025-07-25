'''

Q2. Detect column data types and convert "Age" from float to int

'''

import pandas as pd

data = {
        "Name" : ["A","B","C"],
        "Age" : [21.0,22.0,23.0]
        }

df = pd.DataFrame(data)

print(df.dtypes)

df["Age"] = df["Age"].astype(int)

print(df.dtypes)