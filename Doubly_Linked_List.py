class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def add_from_first(self, data):
        new_node = Node(data)
        if self.head is not None:
           new_node.next = self.head
           self.head.prev = new_node
        self.head = new_node
            
    def add_from_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.next:
            n = n.next
        n.next = new_node
        new_node.prev = n
            
    def delete_from_first(self):
        if self.head is None:
            print("Linked list is Empty. Nothing to delete from.")
        self.head = self.head.next
        
                
    def delete_from_last(self):
        if  self.head is None:
            print("Linked list is Empty. Nothing to delete from.")
        
        n = self.head
        while n.next:
            n = n.next
        n.prev.next = None
                
    def display(self):
        if not self.head:
            print("Linked list is Empty.")
            return
        n = self.head
        
        while n:
            print(n.data, "<-->", end="")
            n = n.next
        print(None)
        self.head.prev=None

if __name__ == "__main__":
    dll = DoublyLinkedList()
    while True:
        print("\nOperation on doubly Linked List.")
        print("\n1. Add from First.\n2. Add from Last.\n3. Delete from First.\n4. Delete from Last.\n5. Display.\n6. Exit.")
        choice = int(input("Enter operation no.:"))
        if choice == 1:
            data = input("Enter element to add from first:")
            dll.add_from_first(data)
        elif choice == 2:
            data = input("Enter element to add from Last:")
            dll.add_from_last(data)
        elif choice == 3:
            try:
                dll.delete_from_first()
            except Exception as e:
                print(e)
        elif choice == 4:
            try:
                dll.delete_from_last()
            except Exception as e:
                print(e)
        elif choice == 5:
            dll.display()
        elif choice == 6:
            break
        else:
            print("Enter valid Operation.")
