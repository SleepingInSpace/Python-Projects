class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_end(data)

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            print("List is empty")
            return

        new_node = Node(data_to_insert)
        current = self.head

        while True:
            if current.data == data_after:
                new_node.next = current.next
                current.next = new_node
                print(f"{data_to_insert} inserted after {data_after}")
                return
            current = current.next
            if current == self.head:
                break

        print(f"Value {data_after} not found in the list")

    def remove_by_value(self, data):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        prev = None
        found = False

        while True:
            if current.data == data:
                found = True
                break
            prev = current
            current = current.next
            if current == self.head:
                break

        if found:
            if prev is None:
                self.head = current.next
            else:
                prev.next = current.next
            print(f"{data} removed from the list")
        else:
            print(f"{data} not found in the list")

    def print_forward(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print()

    def print_backward(self):
        if self.head is None:
            print("List is empty")
            return

        prev = None
        current = self.head
        while prev != self.head:
            prev = current
            current = current.next
        while True:
            print(prev.data, end=" -> ")
            prev = prev.next
            if prev == self.head:
                break
        print()


# Test the Circular Linked List
if __name__ == "__main__":
    LL = CircularLinkedList()
    LL.insert_values(["Red", "Yellow", "Purple", "Orange"])

    print("Forward direction:")
    LL.print_forward()

    LL.insert_after_value("Yellow", "Blue")
    print("Inserted Blue after Yellow:")
    LL.print_forward()

    LL.remove_by_value("Orange")
    print("Removed Orange from the list:")
    LL.print_forward()

    LL.remove_by_value("Green")
    print("Removed Green from the list:")
    LL.print_forward()

    LL.remove_by_value("Red")
    LL.remove_by_value("Yellow")
    LL.remove_by_value("Blue")
    LL.remove_by_value("Purple")
    print("Removed all elements from the list:")
    LL.print_forward()

    print("Printing forward direction after removing all elements:")
    LL.print_forward()

    print("Printing backward direction after removing all elements:")
    LL.print_backward()