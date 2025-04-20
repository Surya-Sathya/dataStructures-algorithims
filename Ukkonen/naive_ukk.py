class Node:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.end_flag =  False

def naive_ukk(str : str) -> Node:
    """
    Input: A string to make into an explicit suffix tree

    Output: The explicit suffix tree for the inputted string

    Runs a naive O(n^3) Ukkonen algorithim, using I(i) to calculate iteratively I(i+1) until I(n). Then n+1th iteration adds -> $
    """ 
    n = len(str)+1

    for phase in range(0,n+1):
        print(phase)


if __name__ == "__main__":
    str = "abcd"
    naive_ukk(str)
