# Annotating Graphs

## Intro to networks and graphs Human genome as a network
Complex systems are often networks of simpler components. In biology, one example are interactions in the human proteome. Just like a genome is all the genes an organism has, the **proteome** is all the proteins an organism can express. The human proteome is not static: while there are around 20,000 genes, each gene can undergo alternative splicing to create multiple proteins. Proteins interact with each other to carry out most cellular processes. These protein-protein interactions can be represented mathematically using **protein-protein interaction networks**. Several databases store these interaction networks and update them based on experimental data. In this section, we will use [HIPPIE](http://cbdm-01.zdv.uni-mainz.de/~mschaefer/hippie/index.php) (Human Integrated Protein-Protein Interactome rEference).

One of the key uses of PPI networks is to identify new disease-related proteins in the human proteome. Once we construct a graph based on the PPI data, we can annotate it to hypothesize groups of related genes.

You can download the most recent HIPPIE database [here](http://cbdm-01.zdv.uni-mainz.de/~mschaefer/hippie/hippie_current.txt). It's formatted as a text file with columns for the two interactors and a confidence value assgined based on the number and quality of studies showing a particular interaction.

| Interactor A   | Interactor B | Confidence Score |
| :---:        | :----:  |:----: |      ---: |
| NEB1     | ACTG | 0.73   |
| SRGN     | CD44|  0.65    |
|GRB7      |ERBB2  |0.9   |

We can build a graph using this data. Graphs are made up of edges and vertices. V, or the number of vertices, represents the number of components in the system (in this case, proteins). It is also known as the **size of the network**. E, or the number of edges, represents the number of interactions between components. The data table above is essentially a list of edges and their **weights**. In addition, the interactions are directed from Interactor A to Interactor B. This kind of graph is called an edge-weighted directed graph, or **edge-weighted digraph**. 

### Figure on Graphs labelling their terms

There are multiple packages that can construct graphs for you. Later, we will use one of these (networkX) for simplicity. To start, however, we can write a simple EdgeWeightedDigraph class in Python. The graph will be made up of directed edges:

```python
class DirectedEdge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight
    
    def toString(self):
        return '{} -> {}  {}'.format(v, w, weight)
```

The toString() method prints the edge with its weight so we can visualize the graph later on. 

```python
class EdgeWeightedDigraph:
    def __init__(self, V):
        self.V = V
        self.E = 0
        self.graph = []
        for i in range(V):
            self.graph.append([])
    
    def addEdge(self, v, w, weight):
        self.graph[v].append(DirectedEdge(v, w, weight))
        self.E+=1
    
    def getEdges(self):
        for v in range(self.V):
            for e in self.graph[v]:
                print(e.toString())
```
We can initialize a new version of this graph and add some edges to it to test it out:
    
```python
ewdg = EdgeWeightedDigraph(3)
ewdg.addEdge(0, 1, 0.3)
ewdg.addEdge(0, 2, 0.9)
ewdg.addEdge(1, 2, 0.15)
ewdg.getEdges()
```

This should print: 

```python
0 -> 1  0.3
0 -> 2  0.9
1 -> 2  0.15
```

Another way to represent a graph is an **adjacency matrix**. An adjacency matrix is a square matrix whose elements represent if a pair of vertices are connected. In the case of a weighted graph, the adjacency matrix values are the edge weights. For our sample graph above, the adjacency matrix would look like this:

## Insert adjacency matrix figure here

Moving forward, we'll be using the package NetworkX **Link** to construct and analyze our graphs. We first read in our dataset and construct a list of edges from the DataFrame. Each edge is a tuple (a list that cannot be changed) of the two vertices it connects and its weight.

```python
import pandas as pd 
import networkx as nx
import matplotlib.pyplot as plt

data = pd.read_csv('cleaned_data.csv')
data.head()

edges = []
for i in range(len(data)):
    edge = (data.id_A[i], data.id_B[i], data.weight[i])
    edges.append(edge)
```

The DiGraph class starts out empty, then we add all the edges in the list we just made. 

```python
graph = nx.DiGraph()
graph.add_weighted_edges_from(edges)
```

NetworkX has a large variety of useful functions, including a function that creates an adjacency matrix for us:

```python
A = nx.adjacency_matrix(graph)
```

Networks have several key properties that we can exploit to predict new disease-related genes. 


### Outline:
A. Terms needed to understand graphs: edge betweenness, hubs. Introduce hypotheses of network medicine

Hubs: Non-essential disease genes (representing the majority of all known disease genes) tend to avoid hubs and segregate at the functional periphery of the interactome. In utero essential genes tend to associated with hubs.
Local hypothesis: Proteins involved in the same disease have an increased tendency to interact with each other.
Corollary of the local hypothesis: Mutations in interacting proteins often lead to similar disease phenotypes.

Disease module hypothesis: Cellular components associated with a specific disease phenotype show a tendency to cluster in the same network neighborhood.

Network parsimony principle: Causal molecular pathways often coincide with the shortest molecular paths between known disease-associated components.

Shared components hypothesis: Diseases that share disease-associated cellular components (genes, proteins, metabolites, miRNAs) show phenotypic similarity and comorbidity.

B. Computing these metrics for our graph using NetworkX and python

C. We have a list of Alzheimer's related proteins. We identify disease module using edge betweenness removals (mention Markov clustering as another option)

D. List of non-disease related connecting edges - predict these are disease genes as well.

E. Conclusions and further topics


## Bibliography
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4889822/
http://networksciencebook.com/chapter/2#networks-graphs

Proximity KNN Graph: https://proxi.readthedocs.io/en/latest/tutorials/proxi_example_1.html

Local search algorithms paper

https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.assortativity.k_nearest_neighbors.html?highlight=k%20nearest#networkx.algorithms.assortativity.k_nearest_neighbors