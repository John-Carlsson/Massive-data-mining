# 

import numpy as np
from numpy import percentile
from scipy import stats
import matplotlib.pyplot as plt

age = np.array([23,23,27,27,39,41,47,49,50,52,54,54,56,57,58,58,60,61])
fat = np.array([9.5,26.5,7.8,17.8,31.4,25.9,27.4,27.2,31.2,34.6,42.5,28.8,33.4,30.2,34.1,32.9,41.2,35.7])

print(age.mean(), 'is the mean of age')
print(fat.mean(), 'is the mean of fat')

print(np.median(age), 'is the median of age')
print(np.median(fat), 'is the median of fat')

plt.subplot(1,3,1)
plt.boxplot(fat)
plt.title('boxplot for fat')
plt.subplot(1,3,2)
plt.boxplot(age)
plt.title('boxplot for age')
plt.subplot(1,3,3)
plt.scatter(age,fat, alpha=0.5)
plt.title('scatterplot for X = age anf Y = fat')
#plt.bar_label(['boxplot for fat','boxplot for age', 'scatterplot for X = age anf Y = fat'])

plt.show()



