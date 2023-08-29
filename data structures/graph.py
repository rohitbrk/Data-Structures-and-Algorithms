# graph
class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.edges_dict = {}
        for start, end in self.edges:
            if start in self.edges_dict:
                self.edges_dict[start].append(end)
            else:
                self.edges_dict[start] = [end]

        print(self.edges_dict)


if __name__ == "__main__":
    routes = [("a", "b"), ("a", "c"), ("b", "c"), ("c", "d")]
    route_graph = Graph(routes)

# different types of graphs
class WeightedDirectedGraph:
    def __init__(self, vertices, edges):
        self.adjList = {}
        for i in vertices:
            self.adjList[i] = []
        for (src, dest, weight) in edges:
            self.adjList[src].append(list([dest, weight]))
            
    def printGraph(self):
        print(self.adjList)
        
      
vertices = ["A", "B", "C"]
edges = [("A", "B", 2), ("B", "C", 5), ("A", "C", 10)]
graph = WeightedDirectedGraph(vertices, edges)
graph.printGraph()
        

class UnDirectedGraph:
    def __init__(self, vertices):
        self.adjList = {}
        for i in vertices:
            self.adjList[i] = list([vertex for vertex in vertices if vertex!=i])
            
    def printGraph(self):
        print(self.adjList)
        
      
vertices = ["A", "B", "C"]
graph = UnDirectedGraph(vertices)
graph.printGraph()


class DirectedGraph:
    def __init__(self, vertices, edges):
        self.adjList = {}
        for i in vertices:
            self.adjList[i] = []
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            
    def printGraph(self):
        print(self.adjList)
        
      
vertices = ["A", "B", "C"]
edges = [("A", "B"), ("B", "C"), ("A", "C")]
graph = DirectedGraph(vertices, edges)
graph.printGraph()


class WeightedUnDirectedGraph:
    def __init__(self, vertices, edges):
        self.adjList = {}
        for i in vertices:
            self.adjList[i] = []
        for (src, dest, weight) in edges:
            self.adjList[src].append([dest, weight])
            
    def printGraph(self):
        print(self.adjList)
        
      
vertices = ["A", "B", "C"]
edges = [("A", "B", 3), ("B", "C", 4), ("A", "C", 10)]
graph = WeightedUnDirectedGraph(vertices, edges)
graph.printGraph()
        
