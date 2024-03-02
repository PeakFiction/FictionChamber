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

house_corr = house.corr(method='pearson')
plt.figure(figsize=(12,12))
sns.heatmap(house_corr, annot=True, linewidths=.5, fmt='.2f')

plt.show()