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

passgrad = pd.read_csv('passing_grade.csv')
skor = pd.read_csv('skor_saintek.csv')
univ = pd.read_csv('universitas.csv')
rank = pd.read_csv('rank_prodi.csv')

# Merge rank and passgrad DataFrames
merged_df = pd.merge(rank, passgrad, on='id_prodi', how='inner')

# Calculate peminat_pil1 and peminat_pil2
merged_df['peminat_pil1'] = merged_df['peminat_2018']
merged_df['peminat_pil2'] = merged_df['peminat_2017'] - merged_df['peminat_2018']

# Calculate peminat_total
merged_df['peminat_total'] = merged_df['peminat_pil1'] + merged_df['peminat_pil2']

# Calculate keketatan_2019_expected and keketatan_2018
merged_df['keketatan_2019_expected'] = (merged_df['kapasitas_2019'] / merged_df['peminat_total']) * 100
merged_df['keketatan_2018'] = (merged_df['kapasitas_2018'] / merged_df['peminat_2018']) * 100

# Print the first few rows of the resulting DataFrame
print(merged_df.head())
