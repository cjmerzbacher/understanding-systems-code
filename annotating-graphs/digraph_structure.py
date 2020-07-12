class DirectedEdge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight
    
    def toString(self):
        return '{} -> {}  {}'.format(self.v, self.w, self.weight)
    
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
    
ewdg = EdgeWeightedDigraph(3)
ewdg.addEdge(0, 1, 0.3)
ewdg.addEdge(0, 2, 0.9)
ewdg.addEdge(1, 2, 0.15)
ewdg.getEdges()