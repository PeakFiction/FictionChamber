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

house_clean = house.copy()
# Drop the 'id' column
house_clean = house_clean.drop(columns=['id'])

# Convert the 'date' column to datetime format
house_clean['date'] = pd.to_datetime(house_clean['date'], format='%Y%m%dT%H%M%S')

# Convert to Zip Code
house_clean['zipcode'] = house_clean['zipcode'].astype(str)

print(house_clean.head())

print("#Ordinal Encoding Categories: Categories that have an Inherent Ordering: Condition")
print(house_clean.select_dtypes('object').head())
condition_mapping = {
    'Bad': 1,
    'Poor': 2, 
    'Fair': 3,
    'Good': 4,
    'Excellent': 5
}

print("#Apply Ordinal Encoding to the Condition Column")
house_clean['condition'] = house_clean['condition'].map(condition_mapping)

print("==================================================================")
print("#One Hot Encoding Categories: Categories that have no Inherent Ordering: ZipCodes")
print("#Apply One Hot Encoding to the Zipcode Column")
house_tmp = pd.get_dummies(house_clean[['zipcode']], columns=['zipcode'], prefix='zipcode')
print("Total additional columns:", house_tmp.shape[1])
print(house_tmp.head(3))

print("==================================================================")
print("#Encoding Zip Codes with Ordinal for Better Dimensions")

#Create a list of unique zip codes
unique_zipcodes = house_clean['zipcode'].unique()

#Initialise the Oridinal Encoder
encoder = OrdinalEncoder(categories=[unique_zipcodes])

#Fit and transform the zipcode column
house_clean['zipcode'] = encoder.fit_transform(house_clean[['zipcode']])
print(house_clean.head(3))
