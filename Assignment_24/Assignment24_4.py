'''
Q4. plot a pie chart of subject marks for "Sagar"

'''

import pandas as pd
import matplotlib.pyplot as plt

data = {
        'Name' : ["Amit", "Sagar", "Pooja"],
        'Math' : [85,90,78],
        'Science' : [92,88,80],
        'English' : [75,85,82]
        }

df = pd.DataFrame(data)

print(df)


df_Sagar = df[df["Name"]== "Sagar"]

print(df_Sagar)

df_Sagar = df_Sagar.melt(id_vars ="Name", var_name ="Subject",value_name = "Marks")

print(df_Sagar)

plt.pie(df_Sagar["Marks"],labels = df_Sagar["Subject"])
plt.title("Sagar Marks")
plt.show()


