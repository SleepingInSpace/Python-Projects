class DCLinkedList:
    class Node:
        def __init__(self,data = None,next = None,prev = None):
            self.data = data
            self.next = next
            self.prev = prev
        
    def __init__(self):
        self.header = self.Node()
        self.header.next = self.header
        self.header.prev = self.header
        self.size = 0

    def InsertInBetween(self,element,p,s):
        new = self.Node(element,p,s)
        p.next = new
        s.prev = new
        new.prev = p
        new.next = s
        
        self.size = self.size + 1
        return new

    def traverse(self):
        curr = self.header.next
        for i in range(self.size):
            print(curr.data)
            curr = curr.next

if __name__ == "__main__":
    dcl = DCLinkedList()
    n1 = dcl.InsertInBetween(23,dcl.header,dcl.header.prev)
    n2 = dcl.InsertInBetween(45,n1,dcl.header.next)
    dcl.traverse()