import random

minNum = 1
maxNum = 50
userNum = 0
tries = 1
randomNum = random.randint(minNum, maxNum)

while userNum != randomNum:
    userNum = int(input(f"Guess the number ({minNum}-{maxNum}): "))
    if userNum < minNum or userNum > maxNum:
        print(f"Please enter a number between {minNum}-{maxNum}!")
        tries += 1
        continue
    elif userNum == randomNum:
        print(f"You win! The number was {randomNum}")
        print(f"You got it in {tries} tries!")
        break
    elif userNum > randomNum:
        print("Too high!")
        tries += 1
    else:
        print("Too low!")
        tries += 1