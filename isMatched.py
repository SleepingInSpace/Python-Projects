class ArrayStack:
    def __init__(self):
        self.data = [None]
        self.size = 0
    def push(self,element):
        self.data.append(element)
        self.size = self.size + 1

    def pop(self):
        if self.size == 0:
            print('Stack Underflow!!')
            return
        self.size = self.size - 1
        return self.data.pop()
    
    def isEmpty(self):
        if self.size == 0:
            return True
    
def isMatched(list):
    stack = ArrayStack()
    lefty = '[{('
    righty = ']})'
    for i in list:
        if i in lefty:
            stack.push(i)
        elif i in righty:
            if stack.isEmpty():
                return False
            if righty.index(i) != lefty.index(stack.pop()):
                return False
    return stack.isEmpty()

if __name__ == "__main__":
    list = "{{()}}"
    print(isMatched(list))