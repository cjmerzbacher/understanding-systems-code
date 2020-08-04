import pandas as pd 
import networkx as nx
import matplotlib.pyplot as plt

#Construct simple graph to show linkages
smallgraph = nx.fast_gnp_random_graph(20, 0.3)
plt.figure()
nx.draw_kamada_kawai(smallgraph)
plt.show()

#Create adjacency matrix
A = nx.adjacency_matrix(smallgraph)
