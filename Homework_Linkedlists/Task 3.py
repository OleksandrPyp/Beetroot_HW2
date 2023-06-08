#Task 3 Queue and Linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def en_queue(self, item):
        temp = Node(item)
        if self.rear is None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def de_queue(self):
        if self.is_empty():
            return
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None

