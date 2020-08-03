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

als_gene_list = ['APP','BACE1','PSEN1','MAPT','APOE','SNCA','PSEN2',
'C9orf72','BDNF','GRN','TARDBP','LRRK2','PRNP','PARK2','SORL1',
'CLU','GSK3B','NOTCH3','TOMM40','IDE','SOD1','PICALM','TREM2',
'CHAT','PINK1','CDK5','NCSTN','BCHE','CYP46A1','BACE2','DYRK1A',
'LRP1','HTT','A2M','COMT','APBB1','CALHM1','ITM2B','IL1A','VCP',
'PIN1','PARK7','CR1','CST3','CHRNA7','CTSD','ADAM10','FUS','ACE',
'IL1B']

#Metrics to consider and compute: connectivity degree, betweenness centrality, closeness centrality, eigenvector centrality, eccentricity

#Identify disease module using edge betweenness removals (mention Markov clustering as another option)

betweenness_centralities = nx.betweenness_centrality(graph, 50)

#Compute in and out degrees
in_degrees = graph.in_degree()
out_degrees = graph.out_degree()

def cluster_edge_betweenness(iterations, G):
    for i in range(iterations):
        eb = nx.edge_betweenness_centrality(G, 10)
        max_eb = max(eb, key=eb.get)
        G.remove_edge(max_eb[0], max_eb[1])
    return G

def calc_proportion_disease_genes(G):


#Compute length of connected components
[len(c) for c in sorted(nx.kosaraju_strongly_connected_components(graph), key=len, reverse=True)]

#Find component for each disease gene

#Compute number of disease genes in each component
nx.node_connected_component(graph, )
