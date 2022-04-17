"""
Analizing CSV file
"""

import pandas as pd

grades = pd.read_csv('2015-2016_Demographic_Data_-_Grades_K-8_School.csv')

print(grades.columns)
