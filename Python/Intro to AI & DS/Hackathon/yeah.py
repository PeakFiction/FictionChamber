import pandas as pd
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Read the dataset
df = pd.read_csv('dataset.csv')

# Filter out English text
english_df = df[df['Language'] == 'English']

# Function for text cleaning
def clean_text(text):
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Lowercasing
    tokens = [token.lower() for token in tokens]
    
    # Remove special characters and numbers
    tokens = [re.sub(r'[^a-zA-Z]', '', token) for token in tokens]
    
    # Remove stopwords
    stopwords_en = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stopwords_en]
    
    # Join tokens back into text
    cleaned_text = ' '.join(tokens)
    
    return cleaned_text

# Apply cleaning function to the 'Text' column
english_df['Cleaned_Text'] = english_df['Text'].apply(clean_text)

# Print the cleaned data
print(english_df[['Text', 'Cleaned_Text']])
