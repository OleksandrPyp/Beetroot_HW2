#task1 The Guessing game

import random

answer = random.randint(1,10)
question = 'Choose the number between 1 and 10 '
print ('Let\'s play the guessing game!')

while True:
    guess = int(input(question))

    if guess < answer:
        print ('Little higher')
    elif guess > answer:
        print ('Little lower')
    else:
        print ('Congratulations, you have guessed correctly!')
        break

#task2 The birthday greeting program

name = input("Plese enter your name ")
age = int(input("Please enter you age "))
new_age = age + 1

print(f"Hello {name}, on your next birthday you'll be {new_age} years old ")

#task3 Words combination 1st try

input_string = input("Please input any word ")
print(''.join(random.sample(input_string,len(input_string))))

#task3 2nd attempt

another_input_str = input("Please input any word:  ")
for i in range(0, len(another_input_str)):
    print("".join(random.sample(another_input_str,len(another_input_str))))
