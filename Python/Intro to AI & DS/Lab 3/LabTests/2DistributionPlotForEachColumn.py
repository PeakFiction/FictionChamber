import numpy as np
import pandas as pd
import urllib.request
from tqdm import tqdm
pd.set_option('display.max_columns', None)

# Data visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Feature engineering
from sklearn.preprocessing import OrdinalEncoder

# Modelling
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

#Top 3 of the CSV File
house = pd.read_csv('kc_house_data.csv')

countplot_cols = []
distplot_cols = []

# Loop through columns to identify those with <= 5 unique values for countplot
for col in house.columns:
    if house[col].nunique() <= 5:
        countplot_cols.append(col)

# Loop through columns to identify those with > 5 unique values for distribution plot
for col in house.columns:
    if col not in countplot_cols:
        distplot_cols.append(col)

#Create subplots
fig, axes = plt.subplots(len(countplot_cols) + len(distplot_cols) // 2, 2, figsize=(12,32))
fig.subplots_adjust(hspace=0.5)

for i, col in enumerate(countplot_cols):
    sns.countplot(data=house, x=col, ax=axes[i//2, i % 2])
    axes[i//2, i%2].set_title(f'{col} distribution (countplot)')

for i, col in enumerate(distplot_cols):
    sns.histplot(data=house, x=col, ax=axes[(i + len(countplot_cols)) // 2, (i + len(countplot_cols)) % 2], bins=20)
    axes[(i + len(countplot_cols)) // 2, (i + len(countplot_cols)) % 2].set_title(f'{col} Distribution (Histogram)')

plt.tight_layout()
plt.show()