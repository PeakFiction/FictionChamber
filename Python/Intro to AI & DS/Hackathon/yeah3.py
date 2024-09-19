import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

df = pd.read_csv('dataset.csv')
df.head(5)

X_text = df['Text'].tolist()
languages = df['Language'].tolist()

text_language_pairs = list(zip(X_text, languages))

print(text_language_pairs[:5])

import re
import spacy
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords


nltk.download('stopwords')

nlp = spacy.load('en_core_web_sm')


stop_words = set(stopwords.words('english'))


def remove_stopwords(text):
    doc = nlp(text)
    return ' '.join(token.text for token in doc if token.text.lower() not in stop_words)

def filter_text(text):
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'#\S+', '', text)
    text = re.sub(r'@\S+', '', text)
    return text

def apply_lemmatization(text):
    doc = nlp(text)
    lemmatized = [token.lemma_ for token in doc]
    return ' '.join(lemmatized)

processed_texts = []
for text, lang in text_language_pairs:
    if lang == 'English':
        processed_text = filter_text(text)
        processed_text = remove_stopwords(processed_text)
        processed_text = apply_lemmatization(processed_text)

        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(processed_text)
        tokens = [token.lower() for token in tokens if token != 'br']
        processed_texts.append(tokens)

print(processed_texts)


from nltk.tokenize import RegexpTokenizer


def tokenize_indonesian(text):
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    return [token.lower() for token in tokens if token != 'br']

processed_texts_indonesian = []
for text, lang in text_language_pairs:
    if lang == 'Indonesian':
        processed_text = filter_text(text)
        processed_text = remove_stopwords(processed_text)
        processed_text = apply_lemmatization(processed_text)
        tokens = tokenize_indonesian(processed_text)
        processed_texts_indonesian.append(tokens)

print(processed_texts_indonesian)

