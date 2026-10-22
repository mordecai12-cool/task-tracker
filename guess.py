import random

secret = random.randint(1, 10)

guess = int(input("Your guess 😊️: ")) 

tries = 1

while guess != secret:
    if guess > secret:
        print("Too high! 🤔️")
    else:
        print("Too low! 🤔️")
    guess = int(input("Your guess 😊️: "))

    tries = tries +1

print("You got it 🥳️👍️! in", tries, "tries")