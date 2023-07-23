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
