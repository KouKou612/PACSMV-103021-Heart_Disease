from Preprocessing import *

"""
0: 'age'
3: 'resting_blood_pressure'
4: 'cholesterol'
7: 'max_heart_rate_achieved'
9: 'st_depression'
11: 'ca'
"""
# All visualizations follow same format


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
    
sigma = 2 
normal_smooth = gaussian_filter1d(normal_counts, sigma=sigma)
disease_smooth = gaussian_filter1d(disease_counts, sigma=sigma)
plt.plot(x_pos - bar_width/2, normal_smooth, color='darkblue', linewidth=3, label='Normal Trend')
plt.plot(x_pos + bar_width/2, disease_smooth, color='darkred', linewidth=3, label='Disease Trend')

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
plt.savefig(os.path.join('Visualization_Figures/Numerical', 'Age_Comparsion.png'), dpi=300)
plt.close()



# Resting Blood Pressure
bp_bins = [90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
bp_groups = ['90-99', '100-109', '110-119', '120-129', '130-139', '140-149', 
             '150-159', '160-169', '170-179', '180-189', '190+']

normal_counts = pd.cut(normal['resting_blood_pressure'], bins=bp_bins, labels=bp_groups).value_counts().reindex(bp_groups, fill_value=0)
disease_counts = pd.cut(disease['resting_blood_pressure'], bins=bp_bins, labels=bp_groups).value_counts().reindex(bp_groups, fill_value=0)

bar_width = 0.35
x_pos = np.arange(len(bp_groups))

plt.bar(x_pos - bar_width/2, normal_counts, bar_width, color=normal_color, 
        edgecolor='black', label='Normal Patients', alpha=0.7)
plt.bar(x_pos + bar_width/2, disease_counts, bar_width, color=disease_color, 
        edgecolor='black', label='Heart Disease Patients', alpha=0.7)

sigma = 2 
normal_smooth = gaussian_filter1d(normal_counts, sigma=sigma)
disease_smooth = gaussian_filter1d(disease_counts, sigma=sigma)
plt.plot(x_pos - bar_width/2, normal_smooth, color='darkblue', linewidth=3, label='Normal Trend')
plt.plot(x_pos + bar_width/2, disease_smooth, color='darkred', linewidth=3, label='Disease Trend')

plt.xlabel('Blood Pressure Groups (mm Hg)', fontsize=12)
plt.ylabel('Number of Patients', fontsize=12)
plt.title('Resting Blood Pressure Distribution: Normal vs. Heart Disease Patients', 
          fontsize=16, fontweight='bold')
plt.xticks(x_pos, bp_groups)
plt.legend()

for i, (normal_count, disease_count) in enumerate(zip(normal_counts, disease_counts)):
    if normal_count > 0:
        plt.text(i - bar_width/2, normal_count + 0.5, str(normal_count), 
                 ha='center', va='bottom', fontweight='bold', fontsize=9)
    if disease_count > 0:
        plt.text(i + bar_width/2, disease_count + 0.5, str(disease_count), 
                 ha='center', va='bottom', fontweight='bold', fontsize=9)

plt.tight_layout()
plt.savefig(os.path.join('Visualization_Figures/Numerical', 'Resting_Blood_Pressure_Distribution_Comparsion.png'), 
            dpi=300, bbox_inches='tight')
plt.close()



# Cholesterol
chol_bins = [0, 150, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560, 600]
chol_groups = ['<150', '150-199', '200-239', '240-279', '280-319', '320-359', 
               '360-399', '400-439', '440-479', '480-519', '520-559', '560+']

normal_counts = pd.cut(normal['cholesterol'], bins=chol_bins, labels=chol_groups).value_counts().reindex(chol_groups, fill_value=0)
disease_counts = pd.cut(disease['cholesterol'], bins=chol_bins, labels=chol_groups).value_counts().reindex(chol_groups, fill_value=0)

bar_width = 0.35
x_pos = np.arange(len(chol_groups))

plt.bar(x_pos - bar_width/2, normal_counts, bar_width, color=normal_color, 
        edgecolor='black', label='Normal Patients', alpha=0.7)
plt.bar(x_pos + bar_width/2, disease_counts, bar_width, color=disease_color, 
        edgecolor='black', label='Heart Disease Patients', alpha=0.7)

sigma = 2 
normal_smooth = gaussian_filter1d(normal_counts, sigma=sigma)
disease_smooth = gaussian_filter1d(disease_counts, sigma=sigma)
plt.plot(x_pos - bar_width/2, normal_smooth, color='darkblue', linewidth=3, label='Normal Trend')
plt.plot(x_pos + bar_width/2, disease_smooth, color='darkred', linewidth=3, label='Disease Trend')

plt.xlabel('Cholesterol Groups (mg/dL)', fontsize=12)
plt.ylabel('Number of Patients', fontsize=12)
plt.title('Cholesterol Distribution: Normal vs. Heart Disease Patients', 
          fontsize=16, fontweight='bold')
plt.xticks(x_pos, chol_groups)
plt.legend()

for i, (normal_count, disease_count) in enumerate(zip(normal_counts, disease_counts)):
    if normal_count > 0:
        plt.text(i - bar_width/2, normal_count + 0.5, str(normal_count), 
                 ha='center', va='bottom', fontweight='bold', fontsize=9)
    if disease_count > 0:
        plt.text(i + bar_width/2, disease_count + 0.5, str(disease_count), 
                 ha='center', va='bottom', fontweight='bold', fontsize=9)

plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig(os.path.join('Visualization_Figures/Numerical', 'Cholesterol_Comparison.png'), 
            dpi=300, bbox_inches='tight')
plt.close()



# Max Heart Rate Achieved
heart_rate_bins = [60, 80, 100, 120, 140, 160, 180, 200, 220]
heart_rate_groups = ['60-79', '80-99', '100-119', '120-139', '140-159', '160-179', '180-199', '200+']

normal_counts = pd.cut(normal['max_heart_rate_achieved'], bins=heart_rate_bins, labels=heart_rate_groups).value_counts().reindex(heart_rate_groups, fill_value=0)
disease_counts = pd.cut(disease['max_heart_rate_achieved'], bins=heart_rate_bins, labels=heart_rate_groups).value_counts().reindex(heart_rate_groups, fill_value=0)

bar_width = 0.35
x_pos = np.arange(len(heart_rate_groups))

plt.figure(figsize=(14, 8))

plt.bar(x_pos - bar_width/2, normal_counts, bar_width, color=normal_color, 
        edgecolor='black', label='Normal Patients', alpha=0.7)
plt.bar(x_pos + bar_width/2, disease_counts, bar_width, color=disease_color, 
        edgecolor='black', label='Heart Disease Patients', alpha=0.7)

sigma = 2 
normal_smooth = gaussian_filter1d(normal_counts, sigma=sigma)
disease_smooth = gaussian_filter1d(disease_counts, sigma=sigma)
plt.plot(x_pos - bar_width/2, normal_smooth, color='darkblue', linewidth=3, label='Normal Trend')
plt.plot(x_pos + bar_width/2, disease_smooth, color='darkred', linewidth=3, label='Disease Trend')

plt.xlabel('Maximum Heart Rate Achieved (bpm)', fontsize=12)
plt.ylabel('Number of Patients', fontsize=12)
plt.title('Maximum Heart Rate Distribution: Normal vs. Heart Disease Patients', 
          fontsize=16, fontweight='bold')
plt.xticks(x_pos, heart_rate_groups)
plt.legend()

for i, (normal_count, disease_count) in enumerate(zip(normal_counts, disease_counts)):
    if normal_count > 0:
        plt.text(i - bar_width/2, normal_count + 0.5, str(normal_count), 
                 ha='center', va='bottom', fontweight='bold', fontsize=9)
    if disease_count > 0:
        plt.text(i + bar_width/2, disease_count + 0.5, str(disease_count), 
                 ha='center', va='bottom', fontweight='bold', fontsize=9)

plt.tight_layout()
plt.savefig(os.path.join('Visualization_Figures/Numerical', 'Max_Heart_Rate_Comparison.png'), 
            dpi=300, bbox_inches='tight')
plt.close()



# ST Depression (oldpeak)
st_depression_bins = [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5]
st_depression_groups = ['0.0-0.4', '0.5-0.9', '1.0-1.4', '1.5-1.9', '2.0-2.4', '2.5-2.9', 
                        '3.0-3.4', '3.5-3.9', '4.0-4.4', '4.5-4.9', '5.0-5.4', '5.5-5.9', '6.0+']

normal_counts = pd.cut(normal['st_depression'], bins=st_depression_bins, labels=st_depression_groups).value_counts().reindex(st_depression_groups, fill_value=0)
disease_counts = pd.cut(disease['st_depression'], bins=st_depression_bins, labels=st_depression_groups).value_counts().reindex(st_depression_groups, fill_value=0)

bar_width = 0.35
x_pos = np.arange(len(st_depression_groups))

plt.figure(figsize=(16, 8))

plt.bar(x_pos - bar_width/2, normal_counts, bar_width, color=normal_color, 
        edgecolor='black', label='Normal Patients', alpha=0.7)
plt.bar(x_pos + bar_width/2, disease_counts, bar_width, color=disease_color, 
        edgecolor='black', label='Heart Disease Patients', alpha=0.7)

sigma = 2 
normal_smooth = gaussian_filter1d(normal_counts, sigma=sigma)
disease_smooth = gaussian_filter1d(disease_counts, sigma=sigma)
plt.plot(x_pos - bar_width/2, normal_smooth, color='darkblue', linewidth=3, label='Normal Trend')
plt.plot(x_pos + bar_width/2, disease_smooth, color='darkred', linewidth=3, label='Disease Trend')

plt.xlabel('ST Depression Groups (mm)', fontsize=12)
plt.ylabel('Number of Patients', fontsize=12)
plt.title('ST Depression Distribution: Normal vs. Heart Disease Patients', 
          fontsize=16, fontweight='bold')
plt.xticks(x_pos, st_depression_groups)
plt.legend()

for i, (normal_count, disease_count) in enumerate(zip(normal_counts, disease_counts)):
    if normal_count > 0:
        plt.text(i - bar_width/2, normal_count + 0.5, str(normal_count), 
                 ha='center', va='bottom', fontweight='bold', fontsize=9)
    if disease_count > 0:
        plt.text(i + bar_width/2, disease_count + 0.5, str(disease_count), 
                 ha='center', va='bottom', fontweight='bold', fontsize=9)

plt.tight_layout()
plt.savefig(os.path.join('Visualization_Figures/Numerical', 'ST_Depression_Comparison.png'), 
            dpi=300, bbox_inches='tight')
plt.close()












