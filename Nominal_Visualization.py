from Preprocessing import *

"""
1: 'sex'
2: 'chest_pain_type'
5: 'fasting_blood_sugar'
6: 'rest_ecg'
8: 'exercise_induced_angina'
10: 'st_slope'
12: 'thalassemia'
"""
# All visualizations follow same format


# Sex
normal_sex_counts = normal['sex'].value_counts().sort_index()
disease_sex_counts = disease['sex'].value_counts().sort_index()

fig, axes = plt.subplots(1, 2, figsize=(12,6))

# Normal Patients Sex Count
axes[0].bar(['Female', 'Male'], normal_sex_counts, color=normal_color, edgecolor='black')
axes[0].set_title('Normal Patients by Sex', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Count')
for i, count in enumerate(normal_sex_counts):
    axes[0].text(i, count + 0.5, str(count), ha='center', va='bottom', fontweight='bold')
    
# Heart Disease Patients Sex Count
axes[1].bar(['Female', 'Male'], disease_sex_counts, color=disease_color, edgecolor='black')
axes[1].set_title('Heart Disease Patients by Sex', fontsize=12, fontweight='bold')
axes[1].set_ylabel('Count')
for i, count in enumerate(disease_sex_counts):
    axes[1].text(i, count + 0.5, str(count), ha='center', va='bottom', fontweight='bold')
    
fig.suptitle('Sex Distributions', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join('Visualization_Figures/Nominal', 'Sex.png'), dpi=300)
plt.close() 



# Chest Pain
chest_pain_categories = ['typical angina', 'atypical angina', 'non-angina pain', 'asymptomatic']
normal_cp_counts = normal['chest_pain_type'].value_counts().reindex(chest_pain_categories, fill_value=0)
disease_cp_counts = disease['chest_pain_type'].value_counts().reindex(chest_pain_categories, fill_value=0)

fig, axes = plt.subplots(1, 2, figsize=(12,6))

# Normal Patients Chest Pain Count
axes[0].bar(chest_pain_categories, normal_cp_counts, color=normal_color, edgecolor='black')
axes[0].set_title('Normal Patients by Chest Pain', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Count')
axes[0].tick_params(axis='x', rotation=15) 
for i, count in enumerate(normal_cp_counts):
    axes[0].text(i, count + 0.5, str(count), ha='center', va='bottom', fontweight='bold')
    
# Heart Disease Patients Chest Pain Count
axes[1].bar(chest_pain_categories, disease_cp_counts, color=disease_color, edgecolor='black')
axes[1].set_title('Heart Disease Patients by Chest Pain', fontsize=12, fontweight='bold')
axes[1].set_ylabel('Count')
axes[1].tick_params(axis='x', rotation=15) 
for i, count in enumerate(disease_cp_counts):
    axes[1].text(i, count + 0.5, str(count), ha='center', va='bottom', fontweight='bold')
    
fig.suptitle('Chest Pain Distributions', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join('Visualization_Figures/Nominal', 'Chest_Pain.png'), dpi=300)
plt.close() 



# Fasting Blood Sugar
normal_fbs_counts = normal['fasting_blood_sugar'].value_counts().sort_index()
disease_fbs_counts = disease['fasting_blood_sugar'].value_counts().sort_index()

fig, axes = plt.subplots(1, 2, figsize=(12,6))

# Normal Patients Fasting Blood Sugar Count
axes[0].bar(['fasting > 120', 'fasting <= 120'], normal_fbs_counts, color=normal_color, edgecolor='black')
axes[0].set_title('Normal Patients by Fasting Blood Sugar', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Count')
for i, count in enumerate(normal_fbs_counts):
    axes[0].text(i, count + 0.5, str(count), ha='center', va='bottom', fontweight='bold')
    
# Heart Disease Patients Fasting Blood Sugar Count
axes[1].bar(['fasting > 120', 'fasting <= 120'], disease_fbs_counts, color=disease_color, edgecolor='black')
axes[1].set_title('Heart Disease Patients by Fasting Blood Sugar', fontsize=12, fontweight='bold')
axes[1].set_ylabel('Count')
for i, count in enumerate(disease_fbs_counts):
    axes[1].text(i, count + 0.5, str(count), ha='center', va='bottom', fontweight='bold')
    
fig.suptitle('Fasting Blood Sugar Distributions', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join('Visualization_Figures/Nominal', 'Fasting_Blood_Sugar.png'), dpi=300)
plt.close() 



# Resting ECG
restECG_categories = ['normal', 'Abnormality in ST-T wave', 'left ventricular hypertrophy']
normal_restECG_counts = normal['rest_ecg'].value_counts().reindex(restECG_categories, fill_value=0)
disease_restECG_counts = disease['rest_ecg'].value_counts().reindex(restECG_categories, fill_value=0)

fig, axes = plt.subplots(1, 2, figsize=(12,6))

# Normal Patients Resting ECG Count
axes[0].bar(restECG_categories, normal_restECG_counts, color=normal_color, edgecolor='black')
axes[0].set_title('Normal Patients by Resting ECG', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Count')
axes[0].tick_params(axis='x', rotation=15) 
for i, count in enumerate(normal_restECG_counts):
    axes[0].text(i, count + 0.5, str(count), ha='center', va='bottom', fontweight='bold')
    
# Heart Disease Patients Resting ECG Count
axes[1].bar(restECG_categories, disease_restECG_counts, color=disease_color, edgecolor='black')
axes[1].set_title('Heart Disease Patients by Resting ECG', fontsize=12, fontweight='bold')
axes[1].set_ylabel('Count')
axes[1].tick_params(axis='x', rotation=15) 
for i, count in enumerate(disease_restECG_counts):
    axes[1].text(i, count + 0.5, str(count), ha='center', va='bottom', fontweight='bold')
    
fig.suptitle('Resting ECG Distributions', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join('Visualization_Figures/Nominal', 'Resting ECG.png'), dpi=300)
plt.close() 



# Angina Induced by Exercise
normal_exang_counts = normal['exercise_induced_angina'].value_counts().sort_index()
disease_exang_counts = disease['exercise_induced_angina'].value_counts().sort_index()

fig, axes = plt.subplots(1, 2, figsize=(12,6))

# Normal Patients Angina Induced by Exercise Count
axes[0].bar(['Yes', 'No'], normal_exang_counts, color=normal_color, edgecolor='black')
axes[0].set_title('Normal Patients by Angina Induced by Exercise', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Count')
for i, count in enumerate(normal_exang_counts):
    axes[0].text(i, count + 0.5, str(count), ha='center', va='bottom', fontweight='bold')
    
# Heart Disease Patients Angina Induced by Exercise Count
axes[1].bar(['Yes', 'No'], disease_exang_counts, color=disease_color, edgecolor='black')
axes[1].set_title('Heart Disease Patients by Angina Induced by Exercise', fontsize=12, fontweight='bold')
axes[1].set_ylabel('Count')
for i, count in enumerate(disease_exang_counts):
    axes[1].text(i, count + 0.5, str(count), ha='center', va='bottom', fontweight='bold')
    
fig.suptitle('Angina Induced by Exercise Distributions', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join('Visualization_Figures/Nominal', 'Angina_Induced_by_Exercise.png'), dpi=300)
plt.close() 



# ST Slope
ST_Slope_categories = ['upsloping', 'flat', 'downsloping']
normal_ST_Slope_counts = normal['st_slope'].value_counts().reindex(ST_Slope_categories, fill_value=0)
disease_ST_slope_counts = disease['st_slope'].value_counts().reindex(ST_Slope_categories, fill_value=0)

fig, axes = plt.subplots(1, 2, figsize=(12,6))

# Normal Patients ST Slope Count
axes[0].bar(ST_Slope_categories, normal_ST_Slope_counts, color=normal_color, edgecolor='black')
axes[0].set_title('Normal Patients by ST Slope', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Count')
for i, count in enumerate(normal_ST_Slope_counts):
    axes[0].text(i, count + 0.5, str(count), ha='center', va='bottom', fontweight='bold')
    
# Heart Disease Patients ST Slope Count
axes[1].bar(ST_Slope_categories, disease_ST_slope_counts, color=disease_color, edgecolor='black')
axes[1].set_title('Heart Disease Patients by ST Slope', fontsize=12, fontweight='bold')
axes[1].set_ylabel('Count')
for i, count in enumerate(disease_ST_slope_counts):
    axes[1].text(i, count + 0.5, str(count), ha='center', va='bottom', fontweight='bold')
    
fig.suptitle('ST Slope Distributions', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join('Visualization_Figures/Nominal', 'ST_Slope.png'), dpi=300)
plt.close() 



# Number of Major Vessels (ca)
ca_categories = ['0', '1', '2', '3']
normal_ca_counts = normal['ca'].value_counts().reindex(ca_categories, fill_value=0)
disease_ca_counts = disease['ca'].value_counts().reindex(ca_categories, fill_value=0)

fig, axes = plt.subplots(1, 2, figsize=(12,6))

# Normal Patients Number of Major Vessels Count
axes[0].bar(ca_categories, normal_ca_counts, color=normal_color, edgecolor='black')
axes[0].set_title('Normal Patients by Number of Major Vessels', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Count')
for i, count in enumerate(normal_ca_counts):
    axes[0].text(i, count + 0.5, str(count), ha='center', va='bottom', fontweight='bold')
    
# Heart Disease Patients Number of Major Vessels Count
axes[1].bar(ca_categories, disease_ca_counts, color=disease_color, edgecolor='black')
axes[1].set_title('Heart Disease Patients by Number of Major Vessels', fontsize=12, fontweight='bold')
axes[1].set_ylabel('Count')
for i, count in enumerate(disease_ca_counts):
    axes[1].text(i, count + 0.5, str(count), ha='center', va='bottom', fontweight='bold')
    
fig.suptitle('Number of Major Vessels Distributions', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join('Visualization_Figures/Nominal', 'Number_of_Major_Vessels_(ca).png'), dpi=300)
plt.close() 



# Thalassemia
thalassemia_categories = ['null', 'fixed defect', 'normal blood flow', 'reversible defect']
normal_thalassemia_counts = normal['thalassemia'].value_counts().reindex(thalassemia_categories, fill_value=0)
disease_thalassemia_counts = disease['thalassemia'].value_counts().reindex(thalassemia_categories, fill_value=0)

fig, axes = plt.subplots(1, 2, figsize=(12,6))

# Normal Patients Thalassemia Count
axes[0].bar(thalassemia_categories[1:4], normal_thalassemia_counts[1:4], color=normal_color, edgecolor='black')
axes[0].set_title('Normal Patients by Thalassemia', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Count')
axes[0].tick_params(axis='x', rotation=15) 
for i, count in enumerate(normal_thalassemia_counts[1:4]):
    axes[0].text(i, count + 0.5, str(count), ha='center', va='bottom', fontweight='bold')
    
# Heart Disease Patients Thalassemia Count
axes[1].bar(thalassemia_categories[1:4], disease_thalassemia_counts[1:4], color=disease_color, edgecolor='black')
axes[1].set_title('Heart Disease Patients by Thalassemia', fontsize=12, fontweight='bold')
axes[1].set_ylabel('Count')
axes[1].tick_params(axis='x', rotation=15) 
for i, count in enumerate(disease_thalassemia_counts[1:4]):
    axes[1].text(i, count + 0.5, str(count), ha='center', va='bottom', fontweight='bold')
    
fig.suptitle('Thalassemia Distributions', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join('Visualization_Figures/Nominal', 'Thalassemia.png'), dpi=300)
plt.close() 