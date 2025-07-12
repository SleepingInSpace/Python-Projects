class MinHeap:
    # MinHeap class implements the MinHeap data structure
    # Heap is a complete binay tree, hence it can be represented using array efficiently
    
    def __init__(self, capacity):
        # constuctor of this initialises a fixed capacity, storing 0 in all the array elements
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0
        
    def getParentIndex(self, index):
        return (index-1)//2
    
    def getLeftChildIndex(self, index):
        return 2*index + 1
        
    def getRightChildIndex(self, index):
        return 2*index + 2
        
    def hasParent(self, index):
        return self.getParentIndex(index) >= 0
        
    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size
    
    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size
    
    def parent(self, index):
        return self.storage[self.getParentIndex(index)]
    
    def leftChild(self, index):
        return self.storage[self.getLeftChildIndex(index)]
        
    def rightChild(self, index):
        return self.storage[self.getRightChildIndex(index)]
    
    def isFull(self):
        return self.size == self.capacity
        
    def swap(self, index1, index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp
    
        
    def insert(self, data):
        # This method adds a new node in MinHeap 
        # if heap is full, then raise Exception
        if(self.isFull()):
            raise Exception("Heap is Full")
        # else add the data as the last element into storage list(underlying storage of MinHeap)
        self.storage[self.size] = data
        self.size += 1
        # New data is added as last element, hence now needs to chceck whether 
        #MinHeap property is satisfied, hence call heapifyUp method
        self.heapifyUp()
    
    def heapifyUp(self):
        index = self.size - 1 # index of the new data
        # current node has a parent and parent node contains value greater than it
        # then swap the values of parent and current node
        while(self.hasParent(index) and self.parent(index) > self.storage[index]):
            self.swap(self.getParentIndex(index), index)
            index = self.getParentIndex(index) # update the current node index as its parent
            
    def removeMin(self):
        # this method deletes the minimum(root node always have minimum value in a MinHeap) value from a MinHeap
        # if heap is empty, then raise exception
        if(self.size == 0):
            raise Exception("Empty Heap")
        # else assign the root node value to data, so that we can return it at the end of this method
        data = self.storage[0]
        # copy the last node value in the root node
        self.storage[0] = self.storage[self.size -1] 
        self.storage[self.size -1] = 0
        # decrement the size by 1
        self.size -= 1
        self.heapifyDown()
        return data
    def removeMax(self):
        # this method deletes the maximum(last node always have maximum value in a MinHeap) value from a MinHeap
        # if heap is empty, then raise exception
        if(self.size == 0):
            raise Exception("Empty Heap")
        # else assign the root node value to data, so that we can return it at the end of this method
        data = self.storage[0]
        # copy the last node value in the root node
        self.storage[0] = self.storage[self.size -1] 
        self.storage[self.size -1] = 0
        # decrement the size by 1
        self.size -= 1
        self.heapifyUp()
        return data
    
    def heapifyDown(self):
        # this method confirms that heap tree still still satisfies the property of MinHeap
        # index is assigned as zero, becuase value is deleted from root, which is stored at index 0
        index = 0 
        # if current node has a left child
        while(self.hasLeftChild(index)):
            # Assume left child has smaller value
            smallerChildIndex = self.getLeftChildIndex(index)
            #if current node has right child, and right child has value smaller than left child
            # then update the smallerChildIndex as right Child index
            if(self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index)):
                smallerChildIndex = self.getRightChildIndex(index)
            
            # current node has smaller value than its smaller child, then heap is a MinHeap, hence break out of loop
            if(self.storage[index] < self.storage[smallerChildIndex]):
                break
            
            else:
                # else swap current node value with its smaller child
                self.swap(index, smallerChildIndex)
                # update the index as smallerChildIndex
                index = smallerChildIndex
                
               
if __name__ == "__main__":
    minH = MinHeap(13)
    minH.insert('Z')
    minH.insert('I')
    minH.insert('J')
    minH.insert('F')
    minH.insert('A')
    minH.insert('E')
    minH.insert('C')
    minH.insert('P')
    minH.insert('B')
    minH.insert('D')
    minH.insert('H')
    minH.insert('N')
    print('minumum value:',minH.removeMin())
    print('maximum value',minH.removeMax())
    print('the heap tree:',minH.storage)