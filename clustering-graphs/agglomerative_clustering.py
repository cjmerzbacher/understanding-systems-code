import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import math

normalized_data = pd.read_csv('cleaned_data.csv')
centroids = []
data = normalized_data.loc[1:10, 't:0':'t:160']

#Calculate nearest neighbor for every point
cats_over_time = []
overall_categories = []
for i in range(len(data)):
    categories = []
    datapt = data.iloc[i]
    min_distance = 800000
    category = 0
    for j in range(len(data)):
        distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(data.iloc[i], datapt)]))
        if distance < min_distance:
            min_distance = distance
            category = j
        categories.append(category)
    overall_categories.append(categories)
    cats_over_time.append(overall_categories)




