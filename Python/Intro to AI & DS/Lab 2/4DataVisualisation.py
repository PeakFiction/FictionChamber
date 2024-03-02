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

plt.figure(figsize=(25,20))
plt.yticks(size=20)

plt.xticks(size=20)

sns.countplot(y='Brand', data=df)

plt.show()