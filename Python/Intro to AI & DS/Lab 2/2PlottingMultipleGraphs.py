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

#KDE Plot for Comparison
yamaha = df[df['Brand'] == 'yamaha']
bmw = df[df['Brand'] == 'bmw']
plt.figure(figsize=(7,5))

#Plots the Torque for Yamaha
sns.kdeplot(yamaha['Torque (Nm)'], fill=True)

#Plots the Torque for BMW
sns.kdeplot(bmw['Torque (Nm)'], fill=True)

plt.legend(['Yamaha', 'BMW'], fontsize=12)
plt.vlines(x=yamaha['Torque (Nm)'].mean(), ymin=0, ymax=0.9, color='blue', linestyles='--')
plt.vlines(x=bmw['Torque (Nm)'].mean(), ymin=0, ymax=0.9, color='brown', linestyle='--')

plt.ylim(0, 0.02)

plt.show()