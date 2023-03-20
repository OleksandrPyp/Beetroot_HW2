#task3
result = list()
y = 0
while y <= 100:
    if y%5 != 0 and y%7 == 0:
        result.append(y)
    y += 7
print(result)
