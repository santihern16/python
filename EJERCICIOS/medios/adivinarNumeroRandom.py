import random

def generateRandomNumber(minNum, maxNum):
    randomNum = random.randint(minNum, maxNum)
    return randomNum

def guessNumber(userNum, randomNum, minNum, maxNum, tries):
        if userNum < minNum or userNum > maxNum:
            print(f"Please enter a number between {minNum}-{maxNum}!")
            return tries + 1, False
        elif userNum == randomNum:
            print(f"You win! The number was {randomNum}")
            print(f"You got it in {tries} tries!")
            return tries, True
        elif userNum > randomNum:
            print("Too high!")
            return tries + 1, False
        else:
            print("Too low!")
            return tries + 1, False

if __name__ == "__main__":
    minNum = 1
    maxNum = 100
    tries = 1

    randomNum = generateRandomNumber(minNum, maxNum)
    
    while True:
        try:
            userNum = int(input(f"Guess the number ({minNum}-{maxNum}): "))
            tries, won = guessNumber(userNum, randomNum, minNum, maxNum, tries)
            if won:
                break
        except ValueError:
            print("Please enter a valid number!")
            tries += 1