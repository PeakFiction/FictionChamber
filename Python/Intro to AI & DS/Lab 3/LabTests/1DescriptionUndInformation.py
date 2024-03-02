# Utils
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
print(house.head(3))

print("==================================================================")
print("#The dimension of the house DataFrame")
print(f"dimension:{house.shape}")

print("==================================================================")
print("#Quick info on the columns")
print(f"{house.info()}")

print("==================================================================")
print("#Numerical Features Description")
print(f"{house.describe(include='number')}")

print("==================================================================")
print("#Object Features Description")
print(f"{house.describe(include='object')}")

print("==================================================================")
print("#Total Unique Values on Each Columns")
print(f"{house.nunique()}")

print("==================================================================")
print("#Check the missing values")
print(f"{house.isnull().sum()}")