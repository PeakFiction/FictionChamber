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
totalrows, total_attributes = df.shape

#Prints its attributes
print(f"Total Number of Rows: {totalrows}")
print(f"Total Number of Attributes: {total_attributes}")
print("================================================")
print(df.head()) #Prints the top 5
print("================================================")
print(df.info()) #Prints the information regarding columns, etc.
print("================================================")
print(df.describe()) #Prints a quick statistic regarding count, mean standard deviation etc. Of the columns
print("================================================")
print(df.describe(include=['object'])) #Same as describe before but only goes for the object type columns
print(df.describe(include=['float64'])) #Same as describe before but only goes for the float64 type columns
print("================================================")

#Creates a series called torqueArray based on the original opened CSV dataFrame, and only the Torque (Nm) column 
torqueArray = df['Torque (Nm)']

#Creates a list based on the stats of torqueArray
stats = [
    ['Mean', np.mean(torqueArray)],
    ['Mode', np.median(torqueArray)],
    ['Mode', scp.mode(torqueArray)[0]],
    ['Standard Deviation', np.std(torqueArray)],
    ['Variance', np.var(torqueArray)],
    ['Minimum', np.min(torqueArray)],
    ['Maximum', np.max(torqueArray)]
]

#makes the stats into a dataframe
torqueDF = pd.DataFrame(stats, columns=['Measure', 'Value'])
print(torqueDF)

print("================================================")

#Plots it as a distribution graph
plt.figure(figsize=(10,5))
sns.kdeplot(torqueArray, fill=True)
plt.vlines(x=np.mean(torqueArray), ymin=0, ymax=1, color='blue', linestyles='--')
plt.vlines(x=np.median(torqueArray), ymin=0, ymax=1, color='brown', linestyle='--')
plt.vlines(x=scp.mode(torqueArray)[0], ymin=0, ymax=1, color='brown', linestyle='--')
plt.legend(['Torque (Nm)', 'Mean', 'Median', 'Mode'], fontsize=12)

plt.ylim(0, 0.01)
plt.show()