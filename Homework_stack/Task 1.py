#Task 1 reverse a sequence of characters using Stack
class Stack:
    def __init__(self):
        self.item = list()

    def empty(self):
        return self.item == []

    def push(self, item):
        self.item.append(item)

    def pop(self):
        return self.item.pop()

    def show(self):
        for item in reversed(self.item):
            print(item)


def insert_bottom(s, item):
    if s.empty():
        s.push(item)
    else:
        popped = s.pop()
        insert_bottom(s, item)
        s.push(popped)


def reverse(s):
    if s.empty():
        pass
    else:
        popped = s.pop()
        reverse(s)
        insert_bottom(s, popped)


stk = Stack()
stk.push(1)
stk.push(9)
stk.show()
reverse(stk)
stk.show()





