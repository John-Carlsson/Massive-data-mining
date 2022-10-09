from turtle import color
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance

x = np.array([[1.5, 1.7], [2, 1.9], [1.6, 1.8], [1.2, 1.5], [1.5, 1.0]])
new_x = np.array([1.4, 1.6])
for a,b in x:
    plt.scatter(a,b, color='r')
plt.scatter(new_x[0], new_x[1])

# euclidian
min_euc = []
for set in x:
    min_euc.append(distance.euclidean(set,new_x))

print('Euclidian: Closest to x %d with distance: %d',np.where(np.where(min_euc==min(min_euc))), min(min_euc))



