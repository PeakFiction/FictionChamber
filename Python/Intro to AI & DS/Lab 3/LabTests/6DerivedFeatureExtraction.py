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

print("Derived feature extraction is the process of creating new features (variables) from existing ones in the dataset")
print("Converting latitude and longitude coordinates into human-readable location information through reverse geocoding can be a useful and informative addition")
import reverse_geocode
lats = house_clean['lat'].to_list()
lons = house_clean['long'].to_list()
coords = list(zip(lats, lons))
print(coords[:5])

print("==================================================================")
print("Examples of reverse geocoding to convert long and lat features")
reversedG = reverse_geocode.search(coords)

cities = []
for loc in reversedG:
    cities.append(loc['city'])
# Can also be: cities = [loc['city'] for loc in reversedG]
print(cities[:5])
print(f"Number of rows: {len(cities)}")
print(f"Number of unique cities: {len(set(cities))}")

print("==================================================================")
print("Trying it out in OrdinalEncoder")

house_clean['city'] = cities

# Create a list of unique cities
unique_cities = house_clean['city'].unique()

# Initialize the OrdinalEncoder
encoder = OrdinalEncoder(categories=[unique_cities])

# Fit and transform the "city" column
house_clean['city'] = encoder.fit_transform(house_clean[['city']])
print(house_clean)

print("==================================================================")
print("Feature Manipulation: The technique of manipulating the value of some features")

print("For example, the \"yr_renovated\" column can be redefined with the following interpretation: a value of 1 indicates that a house has been renovated, while any other value represents 0, indicating no renovation.")

sns.displot(house_clean['yr_renovated'])

house_clean_copy = house_clean.copy()
house_clean_copy['yr_renovated'] = house_clean_copy['yr_renovated'].apply(lambda x:1 if x>0 else 0)
print(house_clean_copy.head(3))