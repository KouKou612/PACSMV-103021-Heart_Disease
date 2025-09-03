import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns
import os
from scipy import stats
from scipy.ndimage import gaussian_filter1d

normal_color = '#66b3ff'
disease_color = '#ff9999'

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12