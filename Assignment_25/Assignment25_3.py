'''
Q3. Apply label Encoding to a "City" column

'''

import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {
    "City" : ["Pune","Mumbai","Delhi","Pune","Delhi"]
}

df = pd.DataFrame(data)

Label_En = LabelEncoder()

df["City_Code"] = Label_En.fit_transform(df["City"])

print(df)

