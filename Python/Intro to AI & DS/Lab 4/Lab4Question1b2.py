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
# Read CSV
df = pd.read_csv("glass.csv")

print("========================================================")
print("Print DataFrame after Changing the Null Values to Zero")
df.fillna(0, inplace=True)
print(df.tail(5))

type_col = df['Type'].to_numpy()
df = df.drop(columns=['Type'])

print("========================================================")
print("Descriptive Statistics of the Dataset")
print(df.describe())

# Calculate correlation matrix
correlation_matrix = df.corr()

# Plot heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap of Glass Dataset Attributes')
plt.show()

# Find top 3 attribute pairs with highest correlation (excluding self-correlation)
correlation_pairs = correlation_matrix.unstack().sort_values(ascending=False)
correlation_pairs = correlation_pairs[correlation_pairs != 1].head(3)

print("========================================================")
print("Top 3 Attribute Pairs with Highest Correlation:")
print(correlation_pairs)
