class Iterable:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter >= len(self.value):
            raise StopIteration
        result = self.value[self.counter]
        self.counter += 1
        return result

    def __getitem__(self, index):
        return self.value[index]


test_var = Iterable([1, 2, 4, 6, 9])

for i in test_var:
    print(i)

print(test_var[1])
