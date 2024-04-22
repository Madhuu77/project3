"""
Created on Wed Apr 17 18:35:21 2024

@author: Madhu.v
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def add_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def add_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
    
    def remove_at_beginning(self):
        if self.head is None:
            print("Linked list empty")
        else:
            self.head = self.head.next
    
    def remove_at_end(self):
        if self.head is None:
            print("Linked list is empty")
        elif self.head.next is None:
            self.head = None
        else:
            prev=None
            n = self.head
            while n.next is not None:
                prev = n
                n = n.next
            prev.n = None
    
    def search(self, x):
        if self.head is None:
            print("\nLinked list is empty")
        else:
            current = self.head
            found = False
            while current is not None and not found:
                if current.data == x:
                    found = True
                else:
                    current = current.next
            if found:
                print("\n", x, " is present in the linked list")
            else:
                print("\n", x, " is not present in the linked list")
                    
    def display(self):
        if self.head is None:
            print("\nLinked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end="")
                n = n.next
            print("\n")
            


sll = SinglyLinkedList()
while True:
    print("*******************************************************\nSelect the operation to perform on the linked list.")
    print("\n1. Add at Beginning\n2. Add at End\n3. Delete at Beginning\n4. Delete at End\n5. Search Node\n6. Display\n7. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = input("\nEnter an element to add at the beginning: ")
        sll.add_at_beginning(data)
        print("\n", data, "is added to the linked list.")
    elif choice == 2:
        data = input("\nEnter an element to add at the end: ")
        sll.add_at_end(data)
        print("\n", data, "is added to the linked list.")
    elif choice == 3:
        sll.remove_at_beginning()
    elif choice == 4:
        sll.remove_at_end()
    elif choice == 5: 
        x = input("\nEnter element to search in the linked list: ")
        sll.search(x)
    elif choice == 6:
        sll.display()
    elif choice == 7:
        break
    else:
        print("\nEnter a valid operation to perform.")
