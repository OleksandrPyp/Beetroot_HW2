#Task 2
class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = list()

    def add_worker(self, worker):
        if isinstance(worker, Worker) and worker not in self._workers:
            self._workers.append(worker)
        else:
            raise ValueError("Can only add Workers")

    def remove_worker(self, worker):
        if isinstance(worker, Worker) and worker in self._workers:
            self._workers.remove(worker)
        else:
            raise ValueError("Can only remove Workers")

    @property
    def workers(self):
        return self._workers


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = boss

    @property
    def boss(self):
        return self.boss

    @boss.setter
    def boss(self, value):
        if not isinstance(value, Boss):
            raise ValueError("Boss must be an instance of a Boss class")
        if self._boss is not None:
            #self._boss.workers.remove(self)
            self.boss = value
            value.add_worker(self)



boss1 = Boss(1, "John", "Company A")
boss2 = Boss(2, "Jane", "Company B")

worker1 = Worker(1, "Alice", "Company A", boss1)
worker2 = Worker(2, "Bob", "Company A", boss1)

print(worker1)
print(worker2)

