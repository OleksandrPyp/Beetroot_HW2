#Task 1
example = input("Please enter the sentence and I will count the repeated words: ")
dictionary = {}
var1 = example.split(" ")

for element in var1:
    if element in dictionary:
        dictionary[element] += 1
    else:
        dictionary[element] = 1
print(dictionary)