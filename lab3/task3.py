import random

num = random.randint(0, 20)
while True:
    guess = int(input("Please type a number: "))
    if guess > num:
        print("You typed too big number!")
    elif guess < num:
        print("You typed too small number!")
    else:
        print("You guessed!")
        break