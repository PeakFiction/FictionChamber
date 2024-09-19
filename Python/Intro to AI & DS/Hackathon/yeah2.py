import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
nltk.data.path.append("/Users/muhammad.sakhran/nltk_data")

nltk.download('stopwords')

# Continue with your code
from nltk.corpus import stopwords
stop_words_en = set(stopwords.words('english'))