class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self,data):
        newNode = Node(data)
        if self.head:
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def display(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next
    
obj = LinkedList()
obj.insert(4)
obj.insert(5)
obj.insert(6)
obj.display()