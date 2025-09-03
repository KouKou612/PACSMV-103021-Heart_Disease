from Preprocessing import *



normal = df[df['target'] == 0]
disease = df[df['target'] == 1]


# Age (all patients)
plt.xlabel('Age')
plt.ylabel('Heart Disease Count')
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