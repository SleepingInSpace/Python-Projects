class DoublyLinkedList:
    class Node:
        def __init__(self,data = None, next = None, prev = None):
            self.data = data
            self.next = next
            self.prev = prev

    def __init__(self):
        self.header = self.Node()
        self.trailer = self.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0
    
    def insertInBetween(self,e,predecessor,successor):
        new = self.Node(e,predecessor,successor)
        predecessor.next = new
        successor.prev = new
        new.prev = predecessor
        new.next = successor
        self.size = self.size + 1
        print('data p:',predecessor.data)
        print('data s',successor.data)
        return new
    
    def forwardTrversal(self):
        currNode = self.header.next 
        for i in range(self.size):
            print(currNode.data)
            currNode = currNode.next
            


    
if __name__ == "__main__":
    dl = DoublyLinkedList()
    node1 = dl.insertInBetween(23,dl.header, dl.trailer)
    node2 = dl.insertInBetween(34,node1,dl.trailer)
    node3 = dl.insertInBetween(78,node1,node2)
    node4 = dl.insertInBetween(15,node1,node3)
    dl.forwardTrversal()
       


