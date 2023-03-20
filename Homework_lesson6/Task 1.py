#Task1 The greatest number
import random

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