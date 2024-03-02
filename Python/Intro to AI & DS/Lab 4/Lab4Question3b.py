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

# Apply Hierarchical Agglomerative Clustering
k = 3
agg_cluster = AgglomerativeClustering(n_clusters=k, linkage='complete')
df_scaled['agg_label'] = agg_cluster.fit_predict(df_scaled)

# Display the first 5 rows of the dataframe with cluster labels
print("========================================================")
print("DataFrame with Agglomerative Clustering Labels")
print(df_scaled.head())

# Plot dendrogram
plt.figure(figsize=(10, 7))
plt.title("Dendrogram")
dend = shc.dendrogram(shc.linkage(df_scaled, method='complete', metric='euclidean'))
plt.show()
