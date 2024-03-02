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
from sklearn.preprocessing import MinMaxScaler


#Read CSV
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

###########################################################################

# Apply Min-Max Scaling to all attributes
scaler = MinMaxScaler()
df_scaled = scaler.fit_transform(df)
df_scaled = pd.DataFrame(df_scaled, columns=df.columns)

print("========================================================")
print("Print DataFrame after Min-Max Scaling")
print(df_scaled.head())


# Initialize lists to store silhouette scores
silhouette_scores = []
k_values = range(2, 9)

# Iterate over each value of K
for k in k_values:
    # Initialize KMeans instance
    kmeans = KMeans(n_clusters=k, n_init=10, random_state=30)
    
    # Fit KMeans to the data
    kmeans.fit(df_scaled)
    
    # Calculate silhouette score
    silhouette_avg = silhouette_score(df_scaled, kmeans.labels_)
    
    # Append silhouette score to list
    silhouette_scores.append(silhouette_avg)

# Find the optimal value of K with the highest silhouette score
optimal_k = k_values[silhouette_scores.index(max(silhouette_scores))]

print("Optimal value of K:", optimal_k)