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

[len(c) for c in sorted(nx.connected_components(smallgraph), key=len, reverse=True)]


#Make graph with disease genes only
als_gene_list = ['APP','BACE1','PSEN1','MAPT','APOE','SNCA','PSEN2',
'C9orf72','BDNF','GRN','TARDBP','LRRK2','PRNP','PARK2','SORL1',
'CLU','GSK3B','NOTCH3','TOMM40','IDE','SOD1','PICALM','TREM2',
'CHAT','PINK1','CDK5','NCSTN','BCHE','CYP46A1','BACE2','DYRK1A',
'LRP1','HTT','A2M','COMT','APBB1','CALHM1','ITM2B','IL1A','VCP',
'PIN1','PARK7','CR1','CST3','CHRNA7','CTSD','ADAM10','FUS','ACE',
'IL1B']


data = pd.read_csv('cleaned_data.csv')
data.head()
A_data = data.loc[data.A.isin(als_gene_list)]
als_data = A_data.append(data.loc[data.B.isin(als_gene_list)]).reset_index(drop=True)

edges = []
for i in range(len(als_data)):
    edge = (als_data.id_A[i], als_data.id_B[i], als_data.weight[i])
    edges.append(edge)

graph = nx.Graph()
graph.add_weighted_edges_from(edges)

def cluster_edge_betweenness(iterations, G):
    for i in range(iterations):
        eb = nx.edge_betweenness_centrality(G, 10)
        max_eb = max(eb, key=eb.get)
        G.remove_edge(max_eb[0], max_eb[1])
    return G

new_graph = cluster_edge_betweenness(10, graph)

#Compute length of connected components
size_ccs = [len(c) for c in sorted(nx.connected_components(new_graph), key=len, reverse=True)]

#Find component for each disease gene
ccs = []
for i in range(len(als_gene_list)):
    als_gene = als_gene_list[i]
    als_gene_key = als_data.loc[als_data.A == als_gene].id_A.unique()
    if len(als_gene_key) != 0:
        cc = len(nx.node_connected_component(graph, als_gene_key[0]))
        ccs.append(cc)

#Compute proportion
for cc in ccs:
    