import pandas as pd
from k_means import cluster, update, assign
from scipy.spatial.distance import cdist
import numpy as np
import matplotlib.pyplot as plt


ks = [4, 6, 8, 10, 12, 14, 16]

distortions = []
for k in ks:
    print('Number of Clusters:', k)
    print('Clustering...')
    centroids = cluster(k)
    data = pd.read_csv('result_data'+str(k)+'.csv')
    print('Clustering complete! Calculating distortion...')
    distances = []
    for i in range(len(data)):
        centroid = centroids[-1][int(data.iloc[i].closest)]
        datapt = data.loc[i, 't:0':'t:160'].to_list()
        distance = sum([(a - b) ** 2 for a, b in zip(centroid, datapt)])
        distances.append(distance)
    distortion = sum(distances)/len(data)
    distortions.append(distortion)
    print('Distortion', distortion)

plt.figure()
plt.plot(ks, distortions, label='Distortion')
plt.legend(loc='best')
plt.title('Elbow Plot')
plt.show()