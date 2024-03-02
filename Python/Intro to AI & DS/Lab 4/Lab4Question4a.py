import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score
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

# Apply DBSCAN clustering
dbscan = DBSCAN()
df_scaled['dbscan_label'] = dbscan.fit_predict(df_scaled)

# Calculate silhouette score
silhouette_avg = silhouette_score(df_scaled, df_scaled['dbscan_label'])

# Display the silhouette score
print("Average silhouette score:", silhouette_avg)
