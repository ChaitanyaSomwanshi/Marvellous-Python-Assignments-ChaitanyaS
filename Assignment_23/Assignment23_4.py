'''
Q4. Display students who scored more than 85 in Science.

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

print(Line)
print("Name of studnets who scored 85+ in science :")
print(Line)
print (df[df['Science'] > 85])
print(Line)