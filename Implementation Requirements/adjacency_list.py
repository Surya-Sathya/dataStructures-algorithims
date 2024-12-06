class Node():
    def __init__(self, node_num, weight) -> None:
        self.node_num = node_num
        self.next = None
        self.weight = weight

class Graph():
    def __init__(self, num_vertices) -> None:
        self.num_vertices = num_vertices
        self.adj_list = [None] * num_vertices
    
    def add_edge(self, src, des, weight):
            node = Node(des, weight)
            node.next = self.adj_list[src]
            self.adj_list[src] = node
 
            #undirected graph
            node = Node(src, weight)
            node.next = self.adj_list[des]
            self.adj_list[des] = node
    
    def delete_edge(self, src, des):
        #Too complicated to implement right now...
        if self.adj_list[des] == None:
            print("Edge not currently present in graph")

        elif self.adj_list[des].node_num == src:
            self.adj_list[des] = self.adj_list[des].next
        
        else:
            curr = self.adj_list[des]
            while curr.next is not None:
                pass
    
    def search(self, u, v):
        if u > len(self.adj_list) - 1 or v > len(self.adj_list) - 1:
            return "Index to high"

        if self.adj_list[u] == None:
            return "Node not found"

        curr = self.adj_list[u]

        while curr is not None:
            if curr.node_num == v:
                return f"Edge {u}-->{v} found!"
            curr = curr.next
        
        return "Edge not found"

    def print_graph(self):
        for node in range(len(self.adj_list)):
            if self.adj_list[node] is not None:
                curr = self.adj_list[node]
                print(f"{node}:", end = "")
                while curr.next is not None:
                    print(f"{curr.node_num}({curr.weight})-->", end = "")
                    curr = curr.next
                print(f"{curr.node_num}({curr.weight})")
            
            else:
                print(f"{node}:")
        
        return


graph = Graph(4)
graph.add_edge(0, 1, 10)
graph.add_edge(0, 3, 12)
graph.add_edge(3, 1, 13)
graph.add_edge(1, 2, 14)
graph.add_edge(2, 3, 15)
graph.print_graph()
print(graph.search(3, 3))
