#Task 1 unordered list (Implement append, index, pop, insert methods for UnorderedList)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def append(self, item):
        temporary = Node(item)
        if self.head is None:
            self.head = temporary
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = temporary

    def index(self, item):
        current = self.head
        index = 0

        while current is not None:
            if current.value == item:
                return index
            current = current.next
            index += 1
        raise ValueError(f"Item {item} is not in the list")

    def pop(self, index = None):
        if self.is_empty():
            raise IndexError("List is empty")
        if index == 0:
            data = self.head.value
            self.head = self.head.next
            return data
        else:
            previous = None
            current = self.head
            current_index = 0
            while current is not None:
                if current_index == index:
                    data = current.value
                    previous.next = current.next
                    return data
                previous = current
                current = current.next
                current_index += 1
        raise IndexError("Index is out of range")

    def insert(self, index, item):
        if index == 0:
            new_node = Node(item)
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            current_index = 0
            while current is not None:
                if current_index == index - 1:
                    new_node = Node(item)
                    new_node.next = current.next
                    current.next = new_node
                    return
                current = current.next
                current_index += 1

        raise IndexError("Index out of range")

    def slice(self, start, stop):
        if start < 0 or stop > self.size() or start >= stop:
            raise ValueError("Invalid slice range")

        current = self.head
        index = 0
        sliced_list = UnorderedList()
        while current is not None:
            if start <= index < stop:
                sliced_list.append(current.data)
            current = current.next
            index += 1

        return sliced_list
