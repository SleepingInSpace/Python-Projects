# creating Stack with underlying data structure Linked List
class LinkedListStack:
   # creating Node class
    class Node:
        def __init__(self, data = None, next = None):
            self.data = data
            self.next = next
    def __init__(self):
        self.head = None
        self.size = 0
#defining push function
    def push(self, element):
        #creating a newvNode
        newNode = self.Node(element) 
        if newNode == None:
            print("no node created!!")
            return
        #updating the head
        newNode.next = self.head
        self.head = newNode
        #increasing size by 1
        self.size += 1
#defining pop function
    def pop(self):
        deletedval = self.head.data
        #breakind link of the head node and updating the headnode
        self.head = self.head.next
        #decreasing size by 1
        self.size -= 1
        return deletedval

   
# defining the function used for navigating the pages
def PagesNavigation(list):
    #creating stack 1 and stack2 
    stack1 = LinkedListStack()
    stack2 = LinkedListStack()
    #pushing all the 10 pages into the stack1 
    # here we will test our forward and backward functionality on these 10 pages
    for i in range(0,len(list)):
        stack1.push(list[i])
    while(stack1 or stack2):
        # taking '<' or '>' key and forward and backward button from the user
        Key = input("Key:")
        # functionality for forward button or next page button
        if Key == '>':
            if stack1.size > 9  :
                print("no next page available !!") 
            else: 
                stack1.push(stack2.pop()) 
                if stack1.size >= 0:
            
                    print("next page:",stack2.head.data)
            
        # functionality for backward button or previous page button
        elif Key == '<':
            
            if stack1.head == None:
                print("no back page available!!")
            else:
                stack2.push(stack1.pop())
                if stack2.size <= 1:
                    
                    stack2.push(stack1.pop())
                    print("previous page:",stack2.head.data)
                else:
                    print('previous page:',stack2.head.data)
        # if no forward or backward button pressed, show error message        
        else:
            print("error")
            
        

if __name__ == "__main__":
    # the pages for testing the code
    list = ['page1','page2','page3','page4','page5','page6','page7','page8','page9','page10']
    # calling the function
    PagesNavigation(list)
