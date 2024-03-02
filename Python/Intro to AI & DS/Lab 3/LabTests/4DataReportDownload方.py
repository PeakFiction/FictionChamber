import numpy as np
import pandas as pd
import urllib.request
from tqdm import tqdm
pd.set_option('display.max_columns', None)

# Data visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Feature engineering
from sklearn.preprocessing import OrdinalEncoder

# Modelling
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

#Top 3 of the CSV File
house = pd.read_csv('kc_house_data.csv')

import dataprep.eda as de
import bokeh.io
bokeh.io.output_notebook()

from dataprep.eda import plot, plot_correlation, create_report, plot_missing
report = create_report(house)
report.save('/content/report.html')