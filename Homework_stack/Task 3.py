class Stack:
    def __init__(self):
        self.stack = list()

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack.pop()

    def get_from_stack(self, item):
        temp = Stack()
        flag = False

        while not self.is_empty():
            current_item = self.pop()
            if current_item == item:
                flag = True
                break
            else:
                temp.push(current_item)

        while not temp.is_empty():
            self.push(temp.pop())

        if flag:
            return current_item
        else:
            raise ValueError(f"Item {item} not found in a stack")

    def show(self):
        for item in self.stack:
            print(item)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

test_var = stack.get_from_stack(3)
print(test_var)
stack.show()
