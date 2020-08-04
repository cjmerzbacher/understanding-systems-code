#Import required packages
import pandas as pd 
import networkx as nx
import matplotlib.pyplot as plt

#Read in cleaned data
data = pd.read_csv('cleaned_data.csv')
data.head()

#Establish graph using edges from DataFrame
edges = []
for i in range(len(data)):
    edge = (data.id_A[i], data.id_B[i], data.weight[i])
    edges.append(edge)

graph = nx.Graph()
graph.add_weighted_edges_from(edges)

#Create adjacency matrix
A = nx.adjacency_matrix(graph)

#Compute betweenness centralities
betweenness_centralities = nx.betweenness_centrality(graph, 50)

#Compute in and out degrees
degrees = {node:val for (node, val) in graph.degree()}

#Rank nodes by degree and BC
#Create DF from degree, BC
bc_df = pd.DataFrame.from_dict(betweenness_centralities, orient='index', columns=['bc']).reset_index()
degrees_df = pd.DataFrame.from_dict(degrees, orient='index', columns=['degrees']).reset_index()

#Join with original dataframe
df = pd.merge(bc_df, degrees_df, on='index')
data['index'] = [str(data['Unnamed: 0'][i]) for i in range(len(data))]
merge = pd.merge(df, data, on='index', how='inner')


nodes = data.loc[data.id_A.isin(data.id_A.unique().tolist())].drop(columns=['id_B', 'B', 'Unnamed: 0', 'index', 'weight'])
nodes['index'] = [str(data['id_A'][i]) for i in range(len(data))]
merge = pd.merge(df, nodes, on='index', how='inner')

#Sort original dataframe by degree, etc.
merge.sort_values('bc', ascending=False).drop_duplicates()
merge.sort_values('degrees', ascending=False).drop_duplicates()



def cluster_edge_betweenness(iterations, G):
    for i in range(iterations):
        print('Iteration ', i+1 , ' of ', iterations)
        eb = nx.edge_betweenness_centrality(G, 10)
        max_eb = max(eb, key=eb.get)
        G.remove_edge(max_eb[0], max_eb[1])
    return G

new_graph = cluster_edge_betweenness(10, graph)

#List of Alzheimer's related genes
als_gene_list = ['APP','BACE1','PSEN1','MAPT','APOE','SNCA','PSEN2',
'C9orf72','BDNF','GRN','TARDBP','LRRK2','PRNP','PARK2','SORL1',
'CLU','GSK3B','NOTCH3','TOMM40','IDE','SOD1','PICALM','TREM2',
'CHAT','PINK1','CDK5','NCSTN','BCHE','CYP46A1','BACE2','DYRK1A',
'LRP1','HTT','A2M','COMT','APBB1','CALHM1','ITM2B','IL1A','VCP',
'PIN1','PARK7','CR1','CST3','CHRNA7','CTSD','ADAM10','FUS','ACE',
'IL1B']

#Compute length of connected components
size_ccs = [len(c) for c in sorted(nx.connected_components(new_graph), key=len, reverse=True)]

#Find component for each disease gene and compute counts
count_ccs = np.zeros(len(size_ccs))
for i in range(len(als_gene_list)):
    als_gene = als_gene_list[i]
    als_gene_key = als_data.loc[als_data.A == als_gene].id_A.unique()
    if len(als_gene_key) != 0:
        cc = len(nx.node_connected_component(graph, als_gene_key[0]))
        for j in range(len(size_ccs)):
            if cc == size_ccs[j]:
                count_ccs[j] += 1

percent_disease_genes = 100*count_ccs/size_ccs

new_graph = cluster_edge_betweenness(100, new_graph)
