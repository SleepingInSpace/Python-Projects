class ArrayStack:
    def __init__(self, capacity = 0):
        self.data = [] * capacity
        self.size = 0
        self.capacity = capacity

    def push(self, element):
        self.data.append(element)
        self.size += 1
        self.capacity += 1
        
    # def pop(self):
    #     if self.size == 0:
    #         print("Stack Underflow!!!")
    #         return
    #     self.capacity -= 1
    #     self.size -= 1
    #     return self.data.pop()
    
    def isEmpty(self):
        return self.size == 0
    
    def length(self):
        return self.capacity
    
    def top(self):
        if self.size == 0:
            print("Stack Underflow!!!")
            return
        return self.data[self.size-1]

    
if __name__ == "__main__":
    s = ArrayStack()
    s.push(2)
    s.push(4)
    s.push(6)
    s.push(8)
    s.push(10)
    print("Popped data:",s.pop())  
    print("Stack Empty?:",s.isEmpty())
    print("Stack Length:",s.length())
    print("Topmost data:",s.top())
    print("Stack capacity:",s.capacity)
    print(s.data)

