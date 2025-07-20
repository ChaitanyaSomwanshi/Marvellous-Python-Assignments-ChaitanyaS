'''
Q.7 Create a bar plot of students names vs total marks.

'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
        'Name' : ["Amit", "Sagar", "Pooja"],
        'Math' : [85,90,78],
        'Science' : [92,88,80],
        'English' : [75,85,82]
        }

df = pd.DataFrame(data)

df["Total"] = df["Math"] + df["Science"] + df["English"]

print(df)

plt.bar(df["Name"],df["Total"], color="skyblue", edgecolor="black")
plt.xlabel("Name")
plt.ylabel("Total Marks")

plt.title("Marvellous Students Total Marks")

plt.show()
