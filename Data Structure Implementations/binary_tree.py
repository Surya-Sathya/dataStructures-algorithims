# Traversal/Search:
    # perfectly balanced O(log_n) time
    # unbalanced: O(n) time (= worst case).\

#Key Features:
#1) Insert Node
#2) Delete Node
#3) Balance BST

class Node():
    def __init__(self, data):
        self.left_child = None
        self.right_child = None
        self.data = data

class BST():
    def __init__(self, root):
        self.root_node = Node(root)
    
    def insert_node(self, data):
        node = Node(data)
        if self.root_node == None:
            self.root_node = node
            return

        BST_node = self.root_node

        def traversal(node, BST_node):
            if node.data > BST_node.data:
                if BST_node.right_child == None:
                    BST_node.right_child = node
                    return
                
                BST_node = BST_node.right_child
                traversal(node, BST_node)

            if node.data < BST_node.data:
                if BST_node.left_child == None:
                    BST_node.left_child = node
                    return

                BST_node = BST_node.left_child
                traversal(node, BST_node)
            
            if node.data == BST_node.data:
                return
         
        traversal(node, BST_node)
    
    def print_tree(self):
        print(f"Root Node: {self.root_node.data}")
        print(f"Left Root Node: {self.root_node.left_child.data}")
        print(f"Left Left Root Node: {self.root_node.left_child.left_child.data}")
        print(f"Left Right Root Node: {self.root_node.left_child.right_child.data}")
        print(f"Right Root Node: {self.root_node.right_child.data}")
        print(f"Right Left Root Node: {self.root_node.right_child.left_child.data}")
        print(f"Right Right Root Node: {self.root_node.right_child.right_child.data}")
        return
                
if __name__ == '__main__':
    binary_tree = BST(50)
    binary_tree.insert_node(30)
    binary_tree.insert_node(20)
    binary_tree.insert_node(40)
    binary_tree.insert_node(70)
    binary_tree.insert_node(60)
    binary_tree.insert_node(80)
    binary_tree.print_tree()
        