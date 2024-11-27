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
        self.accum = 0

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node 

    def delete_node_at_beginning(self):
        node_to_delete = self.head
        self.head = node_to_delete.next

    def insert_at_end(self, data):
        #When you assign a variable to an object instance, and then you modify an attribute of the variable, the object instance changes asw
        current_node = self.head
        while True:
            if current_node.next is None:
                current_node.next = Node(data, None)
                return
            current_node = current_node.next

    
    def print_linked_list(self):
        if self.head == None:
            print("Linked List is Empty")
            return
        
        current_node = self.head
        while True:
            if current_node.next == None:
                print(f"{current_node.data}")
                return
            print(f"{current_node.data}-->", end =" ")
            current_node = current_node.next
            

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(50)
    ll.insert_at_beginning(150)
    ll.insert_at_beginning(250)
    print("Inserted 3 elements", end = ": ")
    ll.print_linked_list()
    ll.delete_node_at_beginning()
    print("Deleted node at end of linked list", end = ": ")
    ll.print_linked_list()
    ll.insert_at_end(500)
    print("Added node to the end of linked list", end = ": ")
    ll.print_linked_list()