'''

Q4. Apply One-Hot Encoding to a "Department" column.

'''

import pandas as pd

data = {
        "Department" :["HR","IT","Finance","HR","IT"]
}

df = pd.DataFrame(data)

One_Hot_Encoding = pd.get_dummies(df["Department"], prefix= "Dept", dtype = int)

print(One_Hot_Encoding)

