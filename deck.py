class DoubleLinkedList:
    class Node:
        def __init__(self,data = None,next = None,prev = None):
            self.data = data
            self.next = next
            self.prev = prev

    def __init__(self):
        self.header = self.Node()
        self.trailer = self.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def InsertInBetween(self,element,predecessor,successor):
        new = self.Node(element,predecessor,successor)
        predecessor.next = new
        successor.prev = new
        new.next = successor
        new.prev = predecessor
        self.size = self.size + 1
        return new
    
    def DeleteInBetween(self,element):
        predecessor = element.prev
        successor = element.next
        predecessor.next = successor
        successor.prev = predecessor
        delval = element.data
        element.predecessor = element.successor = element.data = None
        self.size = self.size - 1
        return delval
    
    def traverse(self):
        curr = self.header.next
        for i in range(self.size):
            print(curr.data)
            curr = curr.next

class Deque(DoubleLinkedList):

    def EnqueueAtHead(self,element):
        self.InsertInBetween(element,self.header,self.header.next)

    def DequeueAtHead(self):
        if self.size == 0:
            print('underflow')
            return
        self.DeleteInBetween(self.header.next)
    def EnqueueAtTail(self,element):
        self.InsertInBetween(element,self.trailer.prev,self.trailer)

    def DequeueAtTail(self):
        if self.size == 0:
            print('underflow')
            return
        self.DeleteInBetween(self.trailer.prev)
    
if __name__ == "__main__":
    deq = Deque()
    n1 = deq.InsertInBetween(23,deq.header,deq.trailer)
    n2 = deq.InsertInBetween(25,n1,deq.trailer)
    n3 = deq.InsertInBetween(45,n2,deq.trailer)
    print('dequeue',deq.DeleteInBetween(n2))
    deq.traverse()

