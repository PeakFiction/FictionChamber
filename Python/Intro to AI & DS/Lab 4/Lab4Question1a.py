import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import silhouette_samples, silhouette_score
from yellowbrick.cluster import SilhouetteVisualizer
import matplotlib.cm as cm
import scipy.cluster.hierarchy as shc
from sklearn.cluster import AgglomerativeClustering

#Read CSV
df = pd.read_csv("glass.csv")

print("========================================================")
print("Print DataFrame Head, Top 5")
print(df.head())

print("========================================================")
print("Print DataFrame after Dropping Type Column")
type_col = df['Type'].to_numpy()
df = df.drop(columns=['Type'])
print(df.head())

print("========================================================")
print("Print DataFrame after Changing the Null Values as Zero")
df.fillna(0, inplace=True)
print(df.tail(5))