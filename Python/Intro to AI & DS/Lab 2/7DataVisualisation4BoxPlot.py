#Important Imports...
import pandas as pd
import numpy as np
import seaborn as sns
import scipy.stats as scp
import plotly.express as px
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit

#Opens the CSV and reads it, automatically formats it as a DataFrame
df = pd.read_csv('motorcycle_specifications.csv')

brand_counts = df['Brand'].value_counts().sort_values(ascending=False)
top_5_brands = brand_counts.head(5)

df_top_5 = df[df['Brand'].isin(top_5_brands.index)]

plt.figure(figsize=(30,10))
plt.xticks(size=20, rotation=90)
plt.yticks(size=20)
sns.boxplot(data=df_top_5, x='Brand', y='Torque (Nm)')
plt.title('Distributio of Torque Values for Top 5 Brands')
plt.show()