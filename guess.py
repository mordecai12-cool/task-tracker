import random

secret = random.randint(1, 10)

guess = 0

tries = 0

while guess != secret and tries < 5:
    try:
        guess = int(input("Your guess 😊️: "))
    except ValueError:
        print("Please type a number")
        continue

    tries = tries +1
    if guess < 1 or guess > 10:
        print("Out of range! 😞️")
    elif guess > secret:
        print("Too high! 🤔️")
    elif guess < secret:
        print("Too low! 🤔️")
    
if guess == secret:
    if tries == 1:
        print("You got it 🥳️👍️! in", tries, "try")
    else:
        print("You got it 🥳️👍️! in", tries, "tries")
else:
    print("You lost 😓️, the number was", secret)