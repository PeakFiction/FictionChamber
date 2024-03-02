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


#Descriptive Statistics for Dry Weight (kg)
# Mean, Median, Mode, Standard Deviation, Variance, Minimum, Maximum, Range, Q1, Q2, Q3

dryWeightDFProto = df['Dry weight (kg)']

stats = [
    ['Mean', np.mean(dryWeightDFProto)],
    ['Mode', np.median(dryWeightDFProto)],
    ['Mode', scp.mode(dryWeightDFProto)[0]],
    ['Standard Deviation', np.std(dryWeightDFProto)],
    ['Variance', np.var(dryWeightDFProto)],
    ['Minimum', np.min(dryWeightDFProto)],
    ['Maximum', np.max(dryWeightDFProto)],
    ['Range', np.ptp(dryWeightDFProto)],
    ['Q1', np.quantile(dryWeightDFProto, .25)]
    ['Q2', np.quantile(dryWeightDFProto, .50)]
    ['Q3', np.quantile(dryWeightDFProto, .75)]
]

dryWeightDF = pd.DataFrame(stats, columns=['Measure', 'Value'])
print(dryWeightDF)