import random
number = random.randint(1, 100)
while True:
    guess = int(input("Guess the number: "))
    if guess == number:
        print("Correct!")
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")
