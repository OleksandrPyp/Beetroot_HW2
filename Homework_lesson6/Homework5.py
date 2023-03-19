#Task1 The greatest number
import random
import numpy as np

rnd_list = random.sample(range(1,11),10)
max_value = 0
while max(rnd_list)>max_value:
    max_value += max(rnd_list)

print(max_value)

#task1 with only while
rnd_list2 = random.sample(range(1,11),10)
x = 0
max_value1 = rnd_list2[x]
while x < len(rnd_list2):
    if rnd_list2[x] > max_value1:
        max_value1 = rnd_list2[x]
    x += 1
print(max_value1)

#task2 Exclusive common numbers

a = (np.random.choice(10,10,replace=True))
b = (np.random.choice(10,10,replace=True))
c = list()

while len(c) < 10:
    for i in a:
        if i not in b:
            c.append(i)
print((set(c)))

#task3
result = list()
y = 0
while y <= 100:
    if y%5 != 0 and y%7 == 0:
        result.append(y)
    y += 7
print(result)

