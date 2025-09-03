import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns
import os



# age  sex  cp  trestbps  chol  fbs  restecg  thalach  exang  oldpeak  slope  ca  thal  target
df = pd.read_csv('Heart_disease_statlog.csv')

normal = df[df['target'] == 0]
disease = df[df['target'] == 1]

normal_color = '#66b3ff'
disease_color = '#ff9999'

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12