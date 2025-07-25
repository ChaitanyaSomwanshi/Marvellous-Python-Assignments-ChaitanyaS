'''
Q9. Replace values in marks less than 50 with fail using where().

'''

import pandas as pd
import numpy  as np

data = {
    "Marks" : [45,67,88,32,76]
}


df = pd.DataFrame(data)

df["Marks"] = np.where(df["Marks"] < 50,"fail",df["Marks"])

print(df)