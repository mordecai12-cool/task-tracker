import random

secret = random.randint(1, 10)

guess = int(input("Your guess: "))

if secret == guess:
    print("You got it!")
elif guess > secret:
    print("Too high!")
else:
    print("Too low!")