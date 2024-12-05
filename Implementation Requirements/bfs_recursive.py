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


def dfs_stack(adj, u):
    stack = [u]

    while len(stack) > 0:
        visiting = stack.pop()
        if explored[visiting] is False:
            print(f"{visiting} --> ", end = "")
            explored[visiting] = True   #This is a very important step you always forget, 
                                        #if you don't assign True, then you'll keep appending neighbours that you've already appended prior
                                        #LOOP: If you append neighbours 1, 2 from 0 -> you pop 2 -> 2 has a neighbour 0 -> append 1, 2 again
                                        #Its fine if 2 has neighbour zero, you just have to stop it from being added to the stack

            for neighbour in adj[visiting]:
                if explored[neighbour] is False:
                    stack.append(neighbour)

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
print("DFS with recursion:", end = " ")
dfs(adj, 0)

print("\n")

explored = [False for x in adj]
print("DFS with a stack:", end = " ")
dfs_stack(adj, 0)