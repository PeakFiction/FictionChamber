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
print("Print DataFrame after Changing the Null Values to Zero")
df.fillna(0, inplace=True)
print(df.tail(5))

print("========================================================")
print("Descriptive Statistics of the Dataset")
print(df.describe())

# Visualize relationship between attributes
sns.pairplot(df)
plt.show()

# Calculate correlation matrix
correlation_matrix = df.corr()

# Find top 3 attribute pairs with highest correlation (excluding self-correlation)
top_pairs = correlation_matrix.unstack().sort_values(ascending=False)
top_pairs = top_pairs[top_pairs != 1].head(3)

print("========================================================")
print("Top 3 Attribute Pairs with Highest Correlation:")
print(top_pairs)