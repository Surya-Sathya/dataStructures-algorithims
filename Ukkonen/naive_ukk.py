class Node:
    def __init__(self):
        self.edge_label = (None, None)
        self.children = [None for i in range(26)]
        self.leaf_idx = None

def traverse(r, path, phase, str):
    c = str[phase]
    c_idx = ord(str[phase])-97
    node = Node()

    if path[0] > path[-1]:
        if r.children[c_idx] == None:
            print("Rule 2 (c1)")
            node.edge_label = (c_idx,c_idx)
            node.leaf_idx = c_idx
            r.children[c_idx] = node

    else:
        curr = r
        for idx_str in path:
            k = ord(str[idx_str])-97
            curr = curr.children[k]

def naive_ukk(str : str) -> Node:
    """
    Input: A string to make into an explicit suffix tree

    Output: The explicit suffix tree for the inputted string

    Runs a naive O(n^3) Ukkonen algorithim, using I(i) to calculate iteratively I(i+1) until I(n). Then n+1th iteration adds -> $
    """ 
    r = Node()
    str += '$'
    n = len(str)

    for i in range(-1, 0):
        print(f"Phase: i+1={i+1}")

        for j in range(0, i+2):
            if i > j:
                path = list(range(j, i+1))  
            elif i<j:
                path = list(range(j, i-1, -1)) 
            elif i==j:
                path = [j,j]
            print(f"Extend: {path}")

            traverse(r, path, i+1, str)

        print("\n")
    
    print(r.children[0].edge_label)

if __name__ == "__main__":
    str = "abcd"
    naive_ukk(str)
