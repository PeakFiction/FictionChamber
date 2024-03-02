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

#Creates a DataFrame of correlation 
correlation = df.corr(method='pearson', numeric_only=True)

print(correlation)

dryWeight = df["Dry weight (kg)"]
wheelbase = df["Wheelbase (mm)"]
df.plot.scatter(x="Dry weight (kg)", y="Wheelbase (mm)", figsize=(6,4))
#Maps out the gradient line, y = mx+c
c, m = polyfit(dryWeight, wheelbase, 1)
plt.plot(dryWeight, c + m * dryWeight, '-')
plt.show()