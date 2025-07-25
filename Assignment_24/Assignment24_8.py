'''
Q8. Plot a histogram of math marks.

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

df["Status"] = np.where(df["Total"] > 250, "Pass", "Fail")

plt.hist(df["Math"],bins = 5, color = "skyblue", edgecolor = "black")

plt.title("Math Marks")
plt.xlabel("Marks")
plt.grid(True)
plt.show()

print(df)