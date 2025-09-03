from config import *


# extend abbreviation of the attributes
df.columns = ['age', 'sex', 'chest_pain_type', 'resting_blood_pressure', 'cholesterol',
              'fasting_blood_sugar', 'rest_ecg', 'max_heart_rate_achieved',
              'exercise_induced_angina', 'st_depression', 'st_slope','ca','thalassemia','target']
print(df.columns)


# convert number features to categorical features
cp_mapping = {0: 'typical angina', 1: 'atypical angina', 2: 'non-angina pain', 3: 'asymptomatic'}
ecg_mapping = {0: 'normal', 1: 'Abnormality in ST-T wave', 2: 'left ventricular hypertrophy'}
slope_mapping = {0: 'upsloping', 1: 'flat', 2: 'downsloping'}
thal_mapping = {0: 'null', 1: 'fixed defect', 2: 'normal blood flow', 3: 'reversible defect'}
sex_mapping = {1: 'male', 0: 'female'}

df['chest_pain_type'] = df['chest_pain_type'].map(cp_mapping)
df['rest_ecg'] = df['rest_ecg'].map(ecg_mapping)
df['st_slope'] = df['st_slope'].map(slope_mapping)
df['thalassemia'] = df['thalassemia'].map(thal_mapping)
df['sex'] = df['sex'].map(sex_mapping)
print(df.head())

# check missing value
print(df.isna().sum())

