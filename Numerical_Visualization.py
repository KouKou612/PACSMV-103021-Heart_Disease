from Preprocessing import *

"""
0: 'age'
3: 'resting_blood_pressure'
4: 'cholesterol'
5: 'fasting_blood_sugar', 
7: 'max_heart_rate_achieved'
8: 'exercise_induced_angina'
9: 'st_depression'
11: 'ca'
13: 'target'
"""


# Age 
age_bins = [20, 30, 40, 50, 60, 70, 80]
age_groups = ['20-29', '30-39', '40-49', '50-59', '60-69', '70-79']

normal_counts = pd.cut(normal['age'], bins=age_bins, labels=age_groups).value_counts().reindex(age_groups, fill_value=0)
disease_counts = pd.cut(disease['age'], bins=age_bins, labels=age_groups).value_counts().reindex(age_groups, fill_value=0)

bar_width = 0.35
x_pos = np.arange(len(age_groups))


plt.bar(x_pos - bar_width/2, normal_counts, bar_width, color=normal_color, 
        edgecolor='black', label='Normal Patients')
plt.bar(x_pos + bar_width/2, disease_counts, bar_width, color=disease_color, 
        edgecolor='black', label='Heart Disease Patients')
    
plt.xlabel('Age Groups')
plt.ylabel('Number of Patients')
plt.title('Age Distribution: Normal vs. Heart Disease Patients', fontsize=16, fontweight='bold')
plt.xticks(x_pos, age_groups)
plt.legend()

for i, (normal_count, disease_count) in enumerate(zip(normal_counts, disease_counts)):
    plt.text(i - bar_width/2, normal_count + 0.5, str(normal_count), 
             ha='center', va='bottom', fontweight='bold')
    plt.text(i + bar_width/2, disease_count + 0.5, str(disease_count), 
             ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join('Visualization_Figures/Numerical', 'Age_Compare.png'), dpi=300)
plt.close()



# Resting Blood Pressure

