import pandas as pd 
import networkx as nx
import matplotlib.pyplot as plt

data = pd.read_csv('cleaned_data.csv')
data.head()

edges = []
for i in range(len(data)):
    edge = (data.id_A[i], data.id_B[i], data.weight[i])
    edges.append(edge)

graph = nx.DiGraph()
graph.add_weighted_edges_from(edges)

#Create adjacency matrix
A = nx.adjacency_matrix(graph)