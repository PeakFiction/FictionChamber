# Utils
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

# Load data
passgrad = pd.read_csv('passing_grade.csv')
skor = pd.read_csv('skor_saintek.csv')
univ = pd.read_csv('universitas.csv')
rank = pd.read_csv('rank_prodi.csv')

# Function to determine passing grade based on selection criteria
def selection_system(selection: int, percentage: float):
    # Copy the score DataFrame to avoid modifying the original data
    skor_copy = skor.copy()
    
    # Total number of students who took part in UTBK
    total_students = skor_copy['id_siswa'].nunique()
    
    # Iterate over each major
    for idx, grup in tqdm(rank.iterrows(), total=len(rank)):
        # Get major id and capacity
        major_id = grup['id_prodi']
        capacity = grup['kapasitas_2019'] * (total_students / 600000)  # Normalize capacity
        
        # Calculate number of students to admit based on the percentage of capacity
        num_accepted = int(np.ceil(percentage * capacity))
        
        # Filter students who selected this major as their first choice
        first_choice_students = skor_copy[(skor_copy['id_prodi_pil1'] == major_id) & (skor_copy['lolos_jurusan'] == 0)]
        
        # Select top-N students based on overall score
        accepted_student_id = first_choice_students.nlargest(num_accepted, 'rerata_keseluruhan')['id_siswa'].tolist()
        
        # Update 'lolos_jurusan' and 'lolos_univ' for accepted students
        skor_copy.loc[skor_copy['id_siswa'].isin(accepted_student_id), 'lolos_jurusan'] = major_id
        skor_copy.loc[skor_copy['id_siswa'].isin(accepted_student_id), 'lolos_univ'] = grup['id_universitas']
        
        # Exclude accepted students from the second choice selection
        skor_copy = skor_copy[~skor_copy['id_siswa'].isin(accepted_student_id)]
        
        # Filter students who selected this major as their second choice
        second_choice_students = skor_copy[(skor_copy['id_prodi_pil2'] == major_id) & (skor_copy['lolos_jurusan'] == 0)]
        
        # Calculate number of students to admit based on the percentage of capacity
        num_accepted = int(np.ceil((1 - percentage) * capacity))
        
        # Select top-N students based on overall score
        accepted_student_id = second_choice_students.nlargest(num_accepted, 'rerata_keseluruhan')['id_siswa'].tolist()
        
        # Update 'lolos_jurusan' and 'lolos_univ' for accepted students
        skor_copy.loc[skor_copy['id_siswa'].isin(accepted_student_id), 'lolos_jurusan'] = major_id
        skor_copy.loc[skor_copy['id_siswa'].isin(accepted_student_id), 'lolos_univ'] = grup['id_universitas']

# Perform selection process for first choice and second choice
selection_system(selection=1, percentage=0.8)
selection_system(selection=2, percentage=0.2)

# Display the updated DataFrame with acceptance results
print(skor_copy)
