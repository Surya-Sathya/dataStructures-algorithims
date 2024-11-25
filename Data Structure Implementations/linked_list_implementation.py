#Key Features of Linked List Data Structure
    #Insert element at beginning
    #Replace an element at a specific place
    #Delete an element at the beginning

class Node():
    def __init__(self, data) -> None: #This fnc will return nothing
        self.data = data
        self.link = self

first_node = Node(13, )