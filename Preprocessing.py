from config import *


# age  sex  cp  trestbps  chol  fbs  restecg  thalach  exang  oldpeak  slope  ca  thal  target
df = pd.read_csv('Heart_disease_statlog.csv')


# expand abbreviation of the attributes
df.columns = ['age', 'sex', 'chest_pain_type', 'resting_blood_pressure', 'cholesterol',
              'fasting_blood_sugar', 'rest_ecg', 'max_heart_rate_achieved',
              'exercise_induced_angina', 'st_depression', 'st_slope','ca','thalassemia','target']


# save an original one for correlation check
df_original = df.copy()

print(df.columns)


# convert number features to categorical features
cp_mapping = {0: 'typical angina', 1: 'atypical angina', 2: 'non-angina pain', 3: 'asymptomatic'}
ecg_mapping = {0: 'normal', 1: 'Abnormality in ST-T wave', 2: 'left ventricular hypertrophy'}
slope_mapping = {0: 'upsloping', 1: 'flat', 2: 'downsloping'}
thal_mapping = {0: 'null', 1: 'fixed defect', 2: 'normal blood flow', 3: 'reversible defect'}
sex_mapping = {1: 'male', 0: 'female'}
fbs_mapping = {1: 'fasting > 120', 0: 'fasting <= 120'}
exang_mapping = {1: 'angina induced by exercise: Yes', 0: 'angina induced by exercise: No'}
ca_mapping = {0: '0', 1: '1', 2: '2', 3:'3'}

df['chest_pain_type'] = df['chest_pain_type'].map(cp_mapping)
df['rest_ecg'] = df['rest_ecg'].map(ecg_mapping)
df['st_slope'] = df['st_slope'].map(slope_mapping)
df['thalassemia'] = df['thalassemia'].map(thal_mapping)
df['sex'] = df['sex'].map(sex_mapping)
df['fasting_blood_sugar'] = df['fasting_blood_sugar'].map(fbs_mapping)
df['exercise_induced_angina'] = df['exercise_induced_angina'].map(exang_mapping)
df['ca'] = df['ca'].map(ca_mapping)
print(df.head())

# check missing value
print(df.isna().sum())


normal = df[df['target'] == 0]
disease = df[df['target'] == 1]
