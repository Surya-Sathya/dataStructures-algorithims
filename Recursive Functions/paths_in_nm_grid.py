def graph_paths(n, m):
    if n == 1 or m == 1:
        return 1
        
    return graph_paths(n-1, m) + graph_paths(n, m-1)

print(graph_paths(3, 3))