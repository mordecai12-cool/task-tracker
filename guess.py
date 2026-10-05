import random

secret = random.randint(1, 100)   # picks a random whole number from 1 to 100

guess = int(input("Your guess: "))  # asks the user to type; int() turns the text into a number

while guess != secret:            # repeats the indented code as long as the condition is True
    print("Wrong!")
    guess = int(input("Try again: "))