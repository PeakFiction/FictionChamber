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

# Calculate average score for TKA group
skor['rerata_tka'] = skor[['skor_bio', 'skor_fis', 'skor_kim', 'skor_mat']].mean(axis=1)

# Calculate average score for TPS group
skor['rerata_tps'] = skor[['skor_kmb', 'skor_kpu', 'skor_kua', 'skor_ppu']].mean(axis=1)

# Calculate overall average score
skor['rerata_keseluruhan'] = skor[['rerata_tka', 'rerata_tps']].mean(axis=1)