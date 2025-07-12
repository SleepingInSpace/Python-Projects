class LinkedListStack:
    class Node:
        def __init__(self, data = None, next = None):
            self.size = 0
            self.data = data
            self.next = next

    def __init__(self, head = None, size = 0):
        self.head = head
        self.size = 0
    
    def push(self, element):
        newNode = self.Node(element)
        if newNode == None:
            print("No New Node created!!!")
            return
        self.head = newNode
        self.head.next = newNode
        self.size += 1

    def pop(self):
        if self.size == 0:
            print("Stack Underflow!!")
            return
        return self.data[-1]
    
    def traverse(self):
        currentNode = self.head
        while(currentNode):
            print(currentNode.data)
            return
