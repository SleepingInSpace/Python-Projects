class LinkedList:
    class Node:
        def __init__(self,data = None,next = None):
            self.data = data
            self.next = next

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
       
    def insertAtFirst(self,element):
        new = self.Node(element)
        if self.size == 0:
            self.tail = new
        new.next = self.head 
        self.head = new
        self.size = self.size + 1
        
    def insertAtTail(self,element):
        new = self.Node(element)
        if self.size == 0:
            self.head = new
        else:
            self.tail.next = new
        self.tail = new
        self.size = self.size + 1

    def deleteAtHead(self):
        if self.size == 0:
            print("underflow!!!")
            return
        delval = self.head.data
        self.head = self.head.next
        self.size = self.size - 1
        return delval
    
    def deleteAtTail(self):
        if self.size == 0:
            print("underflow!!!")
            return
        elif self.size == 1:
            delval = self.head.data
            self.head = None
            self.tail = None
        delval = self.tail.data
        currnode = self.head
        prevnode = None
        while(currnode):
            if currnode == self.tail:
                break
            else:
                prevnode = currnode
                currnode = currnode.next
        prevnode.next = None 
        self.size = self.size - 1 
        delval = self.tail.data 
        self.tail = prevnode 
        return delval


    
    def traverse(self):
        currentNode = self.head
        while(currentNode):
            print(currentNode.data)
            currentNode = currentNode.next
    
if __name__ == "__main__":
    ll = LinkedList()
    ll.insertAtFirst(2)
    # ll.insertAtFirst(32)
    # ll.insertAtFirst(15)
    # ll.insertAtTail(22)
    # ll.insertAtTail(45)
    # print("delval head:",ll.deleteAtHead())
    # print("delval Tail",ll.deleteAtTail())
    print(ll.traverse())
    