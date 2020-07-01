import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import math

normalized_data = pd.read_csv('cleaned_data.csv')
centroids = []
data = normalized_data.loc[1:, 't:0':'t:160'].reset_index(drop=True)
genes = data

num_iter = len(data)

#Set up data structure
data['active'] = [1 for i in(range(len(data)))]
data['child1'] = [-1 for i in(range(len(data)))]
data['child2'] = [-1 for i in(range(len(data)))]
data['clustersize'] = [1 for i in(range(len(data)))]

#Calculate initial nearest neighbors
nearest_neighbors = []; distances = []
for i in range(len(data)):
    min_distance = 800000
    nearest_neighbor = -1
    for j in range(len(data)):
        if i != j: 
            distance = sum([(a - b) ** 2 for a, b in zip(genes.iloc[i], genes.iloc[j])])
            if distance < min_distance:
                min_distance = distance
                nearest_neighbor = j
    nearest_neighbors.append(nearest_neighbor)
    distances.append(min_distance)

data['nearest'] = nearest_neighbors
data['distance'] = distances

for w in range(num_iter):
    index = w+num_iter
    #Combine closest two points
    closestpair = data.loc[data.distance == data.distance.min()].reset_index()
    clustersize1 = int(closestpair.iloc[0].clustersize)
    clustersize2 = int(closestpair.iloc[1].clustersize)
    vec1 = closestpair.loc[0, 't:0':'t:160'].to_list()
    vec2 = closestpair.loc[1, 't:0':'t:160'].to_list()
    centroid = (np.multiply(clustersize1, vec1) + np.multiply(clustersize2, vec2)) / (clustersize1+clustersize2)

    data['active'][closestpair['index'][0]] = 0
    data['active'][closestpair['index'][1]] = 0
    
    length = len(data)
    min_distance = 800000
    nearest_neighbor = -1
    for j in range(len(data)): 
        if data.iloc[j].active == 1:
            vec1 = data.loc[j, 't:0':'t:160'].to_list()
            distance = float(sum([(a - b) ** 2 for a, b in zip(centroid, vec1)]))
            if distance < min_distance:
                min_distance = distance
                nearest_neighbor = j
            if distance < data.distance[j]:
                data['distance'][j] = distance
                data['nearest'][j] = length

    row = list(centroid)+ [1, closestpair['index'][0], closestpair['index'][1], clustersize1+clustersize2, nearest_neighbor, min_distance]
    
    data.loc[index] = row




