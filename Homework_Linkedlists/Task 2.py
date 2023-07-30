#Task 2 Stack and Linked List
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            return popped_node.value

    def display(self):
        iterated_node = self.head
        if self.is_empty():
            raise ValueError("Stack is empty")
        else:
            while iterated_node is not None:
                print(iterated_node.value, end="")
                iterated_node = iterated_node.next
            return

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.value

