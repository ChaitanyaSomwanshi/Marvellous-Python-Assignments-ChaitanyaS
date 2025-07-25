'''
Q6. Replace multiple values in column using a dictionary.



data = {"Grade" : ["A+","B","A","C","B+"]}

replace as 

"A+" : "Excellent"
"A" : "Very Good"
"B+" : "Good"
"B" : "Average"
"C" : "Poor"


'''

import pandas as pd


data = {"Grade" : ["A+","B","A","C","B+"]}

df = pd.DataFrame(data)

df["Grade"] = df["Grade"].replace({"A+" : "Excellent","A" : "Very Good","B+" : "Good",
"B" : "Average","C" : "Poor"})

print(df)



