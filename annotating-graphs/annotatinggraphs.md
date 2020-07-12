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

## Factor graphs, adjacency matrix

## Graph annotation using KNN

