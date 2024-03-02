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

passgrad = pd.read_csv('passing_grade.csv')
skor = pd.read_csv('skor_saintek.csv')
univ = pd.read_csv('universitas.csv')
rank = pd.read_csv('rank_prodi.csv')

# Calculate average score for TKA group
skor['rerata_tka'] = skor[['skor_bio', 'skor_fis', 'skor_kim', 'skor_mat']].mean(axis=1)

# Calculate average score for TPS group
skor['rerata_tps'] = skor[['skor_kmb', 'skor_kpu', 'skor_kua', 'skor_ppu']].mean(axis=1)

# Calculate overall average score
skor['rerata_keseluruhan'] = skor[['rerata_tka', 'rerata_tps']].mean(axis=1)

#Define a function 'selection_system' that assigns students to majors based on selection criteria
def selection_system(selection: int, percentage: float):
    if 'lolos_univ' not in skor.columns:
        skor['lolos_univ'] = 0
    if 'lolos_jurusan' not in skor.columns:
        skor['lolos_jurusan'] = 0

    unassigned_students = skor[skor['lolos_univ'] == 0].copy()
    unassigned_students['rerata_tka'] = unassigned_students[['skor_bio', 'skor_fis', 'skor_kim', 'skor_mat']].mean(axis=1)
    unassigned_students['rerata_tps'] = unassigned_students[['skor_kmb', 'skor_kpu', 'skor_kua', 'skor_ppu']].mean(axis=1)
    unassigned_students['rerata_keseluruhan'] = unassigned_students[['rerata_tka', 'rerata_tps']].mean(axis=1)
    total_population = len(skor['id_siswa'].unique())
    for major in tqdm(rank['id_prodi']):
        try:
            capacity = rank[rank['id_prodi'] == major]['kapasitas_2019'].iloc[0] / total_population
        except IndexError:
            continue
        num_accepted = int(np.ceil(capacity * percentage * total_population))
        accepted_student_id = unassigned_students[unassigned_students['id_prodi_pil1'] == major].nlargest(num_accepted, 'rerata_keseluruhan').index
        unassigned_students.loc[accepted_student_id, 'lolos_jurusan'] = major
        unassigned_students.loc[accepted_student_id, 'lolos_univ'] = unassigned_students.loc[accepted_student_id, 'id_universitas_pil1']
    return unassigned_students

accepted_students = selection_system(selection=1, percentage=0.8)

# Sort the accepted students DataFrame in descending order based on their overall average scores
accepted_students_sorted = accepted_students.sort_values(by='rerata_keseluruhan', ascending=False)

# Calculate the passing grade for each major
passing_grades = {}
for major in accepted_students_sorted['lolos_jurusan'].unique():
    top_n_scores = accepted_students_sorted[accepted_students_sorted['lolos_jurusan'] == major]['rerata_keseluruhan'].values
    passing_grade = min(top_n_scores)
    passing_grades[major] = passing_grade

# Add a new column named 'passing_grade_predicted' to the DataFrame
accepted_students['passing_grade_predicted'] = accepted_students['lolos_jurusan'].map(passing_grades)

# Display the DataFrame with the new column
print(accepted_students)
