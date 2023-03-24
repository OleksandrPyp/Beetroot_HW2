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