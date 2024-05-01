# -*- coding: utf-8 -*-
"""ds_practical_11.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1F_mb883TkbUR9aHQzd0hlxgsGeRKMHMo
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Boston housing dataset
boston = pd.read_csv("datasets/HousingData.csv")

boston.head()

# Plot scatterplot
plot_cat = ["CRIM", "NOX", "AGE", "DIS", "TAX", "B"]

for i in plot_cat:
    plt.figure(figsize=(4, 3))
    sns.scatterplot(x=boston[i], y=boston['MEDV'], color='blue', marker='o', label='Data Points')
    plt.title(f'Scatterplot {i}')
    plt.xlabel(i)
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.show()

# Plot scatterplot
plt.figure(figsize=(4, 3))
sns.scatterplot(x=boston['CRIM'], y=boston['B'], color='black', marker='o')
plt.title(f'Scatterplot Crime vs B')
plt.xlabel("B")
plt.ylabel('Crime Rate')
plt.grid(True)
plt.show()