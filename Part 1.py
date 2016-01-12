import random

number = random.randint(1, 10)
numChosen = 0

while numChosen != number:
    print('Choose a number between 1 and 10')
    numChosen = input()
    if numChosen < number:
        print('Too low! Guess again')
    if numChosen > number:
        print('Too high! Guess again')
    if numChosen == number:
        break

if numChosen == number:
    print('You guessed it right!')