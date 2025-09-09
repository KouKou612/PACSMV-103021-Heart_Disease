from Preprocessing import *



normal = df[df['target'] == 0]
disease = df[df['target'] == 1]


# Age (all patients)
plt.xlabel('Age')
plt.ylabel('Count')
plt.hist(df['age'], bins=20, edgecolor="black")
plt.title('Age Wise Distribution of All patients', fontsize=16)
plt.savefig(os.path.join('Visualization_Figures', 'Age_All_Patients.png'), dpi=300)
plt.close() 



# Heart Disease Rate
heart_disease_counts = df['target'].value_counts()
labels = ['Normal', 'Heart Disease']
sizes = [heart_disease_counts[0], heart_disease_counts[1]]
colors = [normal_color, disease_color]

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Heart Disease Rate in the Dataset', fontsize=16)
plt.savefig(os.path.join('Visualization_Figures', 'Heart_Disease_Rate.png'), dpi=300)
plt.close() 




# Correlation Check 


'''
Cramér's V: 0.1=Weak, 0.3=Moderate, 0.5=Strong association",
p-value: <0.05=Significant, <0.01=Very significant, <0.001=Highly significant
''' 

# Nominal Variable Chi-Square Test
nominal_vars = ['sex', 'chest_pain_type', 'fasting_blood_sugar', 'rest_ecg', 'exercise_induced_angina', 'st_slope', 'thalassemia']

# DataFrame to Store Correlation Data
df_nominal_corr = pd.DataFrame(columns=['Chi2', 'p-value', 'Degrees of Freedom', 'Cramers V'], index=nominal_vars)

for var in nominal_vars:
    table = pd.crosstab(df_original['target'], df_original[var])
    
    chi2, p, dof, expected = stats.chi2_contingency(table)
    
    n = table.sum().sum()
    cramers_v = np.sqrt(chi2 / (n * (min(table.shape) - 1)))
    
    df_nominal_corr.loc[var] = [chi2, p, dof, cramers_v]
    
    
df_cramersv_sorted = df_nominal_corr.sort_values(by='Cramers V', ascending=True)
df_p_sorted = df_nominal_corr.sort_values(by='p-value', ascending=False)

fig, axes = plt.subplots(1, 2, figsize=(12,6))

# Cramér's V
axes[0].bar(df_cramersv_sorted.index, df_cramersv_sorted['Cramers V'], color=normal_color, edgecolor='black')
axes[0].set_title('Cramér\'s V (Larger Means Strong Association)', fontsize=12, fontweight='bold')
axes[0].tick_params(axis='x', rotation=30) 
for i, cv in enumerate(df_cramersv_sorted['Cramers V']):
    axes[0].text(i, cv + 0.005, f"{cv:.3f}", ha='center', va='bottom', fontweight='bold')
    
# p-value
axes[1].bar(df_p_sorted.index, df_p_sorted['p-value'], color=disease_color, edgecolor='black')
axes[1].set_title('p-value (Smaller Means Significant)', fontsize=12, fontweight='bold')
axes[1].tick_params(axis='x', rotation=30) 
for i, p_val in enumerate(df_p_sorted['p-value']):
    if p_val < 0.001:
        label = "<0.001" 
    else:
        label = f"{p_val:.3f}"
    axes[1].text(i, p_val + 0.01, label, ha='center', va='bottom', fontweight='bold')
    
fig.suptitle('Nominal Data Correlations', fontsize=16, fontweight='bold')

comment_text = "fasting_blood_sugar is not strong and significant, rest_ecg is not Strong, these two should have low feature importance"
fig.text(0.5, 0.01, comment_text, ha='center', va='bottom', fontsize=10, 
         style='italic', wrap=True, bbox=dict(boxstyle="round,pad=0.5", 
         facecolor="lightgray", alpha=0.7))

plt.tight_layout()
plt.savefig(os.path.join('Visualization_Figures', 'Nominal_Correlations.png'), dpi=300)
plt.close() 


    
# Numerical Variables Correlations

"""
STRONG_THRESHOLD = 0.5
MODERATE_THRESHOLD = 0.3
WEAK_THRESHOLD = 0.1
"""
numerical_columns = ['age', 'resting_blood_pressure', 'cholesterol', 'max_heart_rate_achieved', 'st_depression', 'ca', 'target']
df_numerical = df[numerical_columns]

target_correlation = df_numerical.corr()['target'].drop('target')
target_correlation = target_correlation.sort_values(ascending=True)

colors = ['red' if x < 0 else 'blue' for x in target_correlation]
bars = plt.barh(target_correlation.index, target_correlation.values, 
                color=colors, alpha=0.7, edgecolor='black')

for i, (feature, value) in enumerate(zip(target_correlation.index, target_correlation.values)):
    x_pos = value + 0.01 if value >= 0 else value - 0.01
    ha_pos = 'left' if value >= 0 else 'right'
    
    plt.text(x_pos, i, f'{value:.3f}', 
             ha=ha_pos, 
             va='center', 
             fontweight='bold',
             fontsize=12,
             color='black')

plt.axvline(x=0, color='black', linestyle='-', alpha=0.5, linewidth=1)

plt.xlabel('Correlation Coefficient (closer to ±1 means stronger relationship)', fontsize=14, fontweight='bold')
plt.ylabel('Numerical Features', fontsize=14, fontweight='bold')
plt.title('Correlation of Numerical Features with Heart Disease', fontsize=16, fontweight='bold')

x_margin = max(abs(target_correlation.min()), abs(target_correlation.max())) * 0.1
plt.xlim(target_correlation.min() - x_margin, target_correlation.max() + x_margin)

comment_text = "age, resting_blood_pressure, cholestrol have weak correlation, all other variables have moderate correlation"
fig.text(0.5, 0.01, comment_text, ha='center', va='bottom', fontsize=10, 
         style='italic', wrap=True, bbox=dict(boxstyle="round,pad=0.5", 
         facecolor="lightgray", alpha=0.7))

plt.tight_layout()
plt.savefig(os.path.join('Visualization_Figures', 'Numerical_Correlations.png'), 
            dpi=300, bbox_inches='tight')
plt.close()