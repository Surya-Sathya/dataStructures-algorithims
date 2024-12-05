class Graph():
    def __init__(self, vertices) -> None:
        self.vertices = vertices
        self.adj = [[] for x in range(self.vertices)]
    
    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)
    
    def get_adj(self):
        return self.adj

def bfs(adj, u):
    #Create explored array
    explored = [False for x in adj]
    q = [u]
    while len(q) > 0:
        visiting = q.pop(0)
        if explored[visiting] == False:
            explored[visiting] = True
            print(f"{visiting} --> ", end="")
            for neighbour in adj[visiting]:
                if explored[neighbour] == False:
                    q.append(neighbour)
    
    return
 
graph = Graph(10)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(1, 4)
graph.add_edge(1, 3)
graph.add_edge(3, 5)
graph.add_edge(5, 6)
graph.add_edge(5, 7)
graph.add_edge(5, 8)
graph.add_edge(7, 8)
graph.add_edge(8, 9)

adj = graph.get_adj()
bfs(adj, 0)

