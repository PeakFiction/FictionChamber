import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import silhouette_samples, silhouette_score
from yellowbrick.cluster import SilhouetteVisualizer
import matplotlib.cm as cm
import scipy.cluster.hierarchy as shc
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import MinMaxScaler

# Read CSV
df = pd.read_csv("glass.csv")

print("========================================================")
print("Print DataFrame after Changing the Null Values to Zero")
df.fillna(0, inplace=True)
print(df.tail(5))

print("========================================================")
print("Print DataFrame after Dropping Type Column")
type_col = df['Type'].to_numpy()
df = df.drop(columns=['Type'])
print(df.head())

# Apply Min-Max Scaling to all attributes
scaler = MinMaxScaler()
df_scaled = scaler.fit_transform(df)
df_scaled = pd.DataFrame(df_scaled, columns=df.columns)

print("========================================================")
print("Print DataFrame after Min-Max Scaling")
print(df_scaled.head())
###########################################################################

# Initialize lists to store silhouette scores
silhouette_scores = []
k = 3

# Generate permutation of triplets
triplets = list(itertools.combinations(df_scaled.columns, 3))

# Iterate over each triplet
for triplet in triplets:
    # Select the triplet of features
    selected_features = df_scaled[list(triplet)]
    
    # Initialize KMeans instance
    kmeans = KMeans(n_clusters=k, n_init=10, random_state=30)
    
    # Fit KMeans to the data
    kmeans.fit(selected_features)
    
    # Calculate silhouette score
    silhouette_avg = silhouette_score(selected_features, kmeans.labels_)
    
    # Append silhouette score to list
    silhouette_scores.append((triplet, silhouette_avg))

# Find the combination with the highest silhouette score
best_combination = max(silhouette_scores, key=lambda x: x[1])

# Print the best combination
print("Best combination:", best_combination)
