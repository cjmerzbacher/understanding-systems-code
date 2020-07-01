import pandas as pd
import random
import math

#Assign all genes to a cluster using Euclidean distance
def assign(data, centroids):
    categories = []
    for i in range(len(data)):
        datapt = data.iloc[i]
        min_distance = 800000
        category = 0
        for j in range(len(centroids)):
            distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(centroids[j], datapt)]))
            if distance < min_distance:
                min_distance = distance
                category = j
        categories.append(category)
    return categories


#Update centroid positions
def update(data, centroids, k):
    diffs = []
    for j in range(k):
        datacentroid = data.loc[data.closest == j].reset_index(drop=True).loc[1:, 't:0':'t:160']
        coord = []
        for i in datacentroid:
            r = datacentroid[i].mean()
            coord.append(r)
        diff = [abs(a - b) for a, b in zip(centroids[j], coord)]
        diffs.append(diff)
        centroids[j] = coord
    return diffs, centroids

def cluster(k):
    normalized_data = pd.read_csv('cleaned_data.csv')

    #Initialize random centroids (set parameter k)
    centroids = []
    data = normalized_data.loc[1:, 't:0':'t:160']
    for j in range(k):
        coord = []
        for i in data:
            r = random.uniform(data[i].min(), data[i].max())
            coord.append(r)
        centroids.append(coord)

    #Iterate to repeatedly assign and update
    categories = assign(data, centroids)
    data['closest'] = categories
    diffs, centroids = update(data, centroids, k)

    centroid_data = [centroids]
    print(centroids)
    count = 0
    while(max([max(diffs[i]) for i in range(k)]) > 0.05):
        count+=1
        print('Iteration', count)
        categories = assign(data, centroids)
        data['closest'] = categories
        diffs, centroids = update(data, centroids, k)
        #centroid_data.append(centroids)
    data.to_csv('result_data'+str(k)+'.csv')
    #centroid_data.to_csv('centroid_result_data'+str(k)+'.csv')

    return centroids


    



