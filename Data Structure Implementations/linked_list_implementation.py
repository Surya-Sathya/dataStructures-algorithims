#Key Features of Linked List Data Structure
    #Insert element at beginning
    #Replace an element at a specific place
    #Delete an element at the beginning

class Node():
    def __init__(self, data, next) -> None: #This fnc will return nothing
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self) -> None:
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node 
    
    def print_linked_list(self):
        if self.head == None:
            print("Linked List is Empty")
            return

if __name__ == '__main__':
    ll = LinkedList()
    ll.print_linked_list()
    ll.insert_at_beginning(50)