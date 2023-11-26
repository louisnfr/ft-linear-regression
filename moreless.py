import random

answer = random.randint(0, 10)
guess = int(input('enter a number: '))
count = 1

while (guess != answer):
    count += 1
    if guess > answer:
        print('less')
    elif guess < answer:
        print('more')
    guess = int(input('enter a number: '))

print('\nyou found in', count, 'guesses')
