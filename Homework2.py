#task 1
import random

name = "Oleks"
day_of_the_week = "Tuesday"

print("Good day %s, %s is a perfect day to learn some python." %(name,day_of_the_week))

print("Good day {}, {} is a perfect day to learn some python.".format(name, day_of_the_week))

print(f"Good day {name}, {day_of_the_week} is a perfect day to learn some python.")

#task2
first_name = 'Oleksandr'
surname = 'Pypenko'
print(first_name + " " + surname)

print(" ".join([first_name,surname]))

#task3

a = random.randint(0,100)
b = random.randint(0,3)

print('Addition results = ', a+b)
print('Subtraction results = ', a-b)
print('Division results = ', a/b)
print('Multiplication results = ', a*b)
print('Exponent(Power) results = ', a**b)
print('Modulus results = ', a%b)
print('Floor Division results = ', a//b)