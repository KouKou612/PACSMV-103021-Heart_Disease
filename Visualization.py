from Preprocessing import *

"""
0: 'age'
1: 'sex'
2: 'chest_pain_type'
3: 'resting_blood_pressure'
4: 'cholesterol'
5: 'fasting_blood_sugar', 
6: 'rest_ecg'
7: 'max_heart_rate_achieved'
8: 'exercise_induced_angina'
9: 'st_depression'
10: 'st_slope'
11: 'ca'
12: 'thalassemia'
13: 'target'
"""

# Heart Disease Rate
heart_disease_counts = df['target'].value_counts()
labels = ['Normal', 'Heart Disease']
sizes = [heart_disease_counts[0], heart_disease_counts[1]]
colors = ['#66b3ff', '#ff9999']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Heart Disease Rate in the Dataset', fontsize=16)
plt.savefig(os.path.join('PACSMV-103021-Heart_Disease/Visualization_Figures', 'Heart_Disease_Rate.png'), dpi=300)
plt.close() 


# Age 
plt.xlabel('Age')
plt.ylabel('Heart Disease Count')
plt.hist(df['age'], bins=20, edgecolor="black")
plt.title('Age Wise Distribution', fontsize=16)
plt.savefig(os.path.join('PACSMV-103021-Heart_Disease/Visualization_Figures', 'Age.png'), dpi=300)
plt.close() 


# Sex and Age
normal = df[df['target'] == 0]
disease = df[df['target'] == 1]
normal_sex_counts = normal['sex'].value_counts().sort_index()
disease_sex_counts = disease['sex'].value_counts().sort_index()

fig, axes = plt.subplots(1, 2, figsize=(10,8))
normal_color = '#66b3ff'
disease_color = '#ff9999'
# Normal Patients Sex Count
axes[0].bar(['Female', 'Male'], normal_sex_counts, color=normal_color, edgecolor='black')
axes[0].set_title('Normal Patients by Sex', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Count')
for i, count in enumerate(normal_sex_counts):
    axes[0].text(i, count + 0.5, str(count), 
         ha='center', va='bottom', fontweight='bold')
# Heart Disease Patients Sex Count
axes[1].bar(['Female', 'Male'], disease_sex_counts, color=disease_color, edgecolor='black')
axes[1].set_title('Heart Disease Patients by Sex', fontsize=12, fontweight='bold')
axes[1].set_ylabel('Count')
for i, count in enumerate(disease_sex_counts):
    axes[1].text(i, count + 0.5, str(count), 
         ha='center', va='bottom', fontweight='bold')
fig.suptitle('Sex Distributions', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join('PACSMV-103021-Heart_Disease/Visualization_Figures', 'Sex.png'), dpi=300)
plt.close() 


