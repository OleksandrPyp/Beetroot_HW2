#task2 Exclusive common numbers
import numpy as np

a = (np.random.choice(10,10,replace=True))
b = (np.random.choice(10,10,replace=True))
c = list()

#while len(c) <= 10:
for i in a:
     if i in b:
        c.append(i)
print((set(c)))
