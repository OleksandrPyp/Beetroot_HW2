class Queue:
    def __init__(self):
        self.queue = list()

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue.pop(0)

    def get_from_queue(self, item):
        temp_q = Queue()
        flag = False

        while not self.is_empty():
            current_item = self.dequeue()
            if current_item == item:
                flag = True
                break
            else:
                temp_q.enqueue(current_item)

        while not temp_q.is_empty():
            self.enqueue(temp_q.dequeue())

        if flag:
            return current_item
        else:
            raise ValueError(f"Item {item} not found in queue")


q = Queue()
q.enqueue(1)
q.enqueue(4)
q.enqueue(7)
q.enqueue(8)
query = q.get_from_queue(9)
print(query)