# import libraries
#If you're running it on MacOS for the first time, do remember to:
#pip install seaborn
#pip install -U scikit-learn
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sklearn as sklearn

# load iris data
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['class'] = iris.target # 0, 1, 2 correspond to 'setosa', 'versicolor', 'virginica'
print(df)


sns.countplot(x=df['class'])