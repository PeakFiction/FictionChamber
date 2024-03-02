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

#Creating teh base countplots
plt.figure(figsize=(15,10))
plt.yticks(size=20)

plt.xticks(size=20)
# y is label, and data = df
sns.countplot(y='Cooling system', data=df)
plt.show()