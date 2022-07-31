import random


while True:
    try:
        level = input("Level: ")
        if int(level) > 1:
            break
    except ValueError:
        pass

while True:
    r = random.randint(1, int(level))

    try:
        guess = int(input("Guess: "))
        if guess > r:
            print("Too large!")
        elif guess < r:
            print("Too small!")
        else:
            print("just right!")
            break
    except ValueError:
        pass