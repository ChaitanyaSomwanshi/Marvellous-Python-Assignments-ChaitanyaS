'''
Q3. Add a new columm 'Total' to the DataFrame as the sum of all subject marks.

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

df["Total"]= df['Math'] + df['Science']+ df['English']


print(df)