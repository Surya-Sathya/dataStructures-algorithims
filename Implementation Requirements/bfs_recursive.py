class Graph():
    def __init__(self, vertices) -> None:
        self.vertices = vertices
        self.adj = [[] for x in range(self.vertices)]
    
    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)
    
    def get_adj(self):
        return self.adj
    
def dfs(adj, u):
        print(f"{u} --> ", end = "")
        explored[u] = True

        for neighbour in adj[u]:
            if explored[neighbour] is False:
                #print(f"dfs(adj, {neighbour})")
                dfs(adj, neighbour)

graph = Graph(5)
graph.add_edge(0, 1)
graph.add_edge(0, 3)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
adj = graph.get_adj()

#I initially plcaed this explored list INSIDE the dfs algorithim, which resets everything to false, hence infinite loop
explored = [False for x in adj]
dfs(adj, 0)