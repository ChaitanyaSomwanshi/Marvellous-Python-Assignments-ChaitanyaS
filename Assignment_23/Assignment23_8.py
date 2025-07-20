'''
Q.8 Plot a line chart of marks for 'Amit' across all subjects.

'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {
        'Name' : ["Amit", "Sagar", "Pooja"],
        'Math' : [85,90,78],
        'Science' : [92,88,80],
        'English' : [75,85,82]
        }

df = pd.DataFrame(data)

# df["Total"] = df["Math"] + df["Science"] + df["English"]



df_Amit = df[df["Name"]=="Amit"]

print(df_Amit)

# unpivot 

df_Amit_reshape = df_Amit.melt(id_vars=["Name"],var_name = "Subject",value_name="Marks")

plt.figure(figsize=(8,5))

sns.lineplot(data=df_Amit_reshape,x="Subject",y="Marks")

plt.xlabel("Subject")
plt.ylabel("Marks")
plt.title("Amit marks across all subjects")

plt.show()