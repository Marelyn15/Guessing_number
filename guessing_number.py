import random
from art import logo


print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

random_number = random.randint(1,100)
if difficulty == 'easy':
    # Attemps
    attemps = 10
    while attemps > 0:
        print(f"You have {attemps} remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == random_number:
            print(f"Very well. You guessed the number {guess}")
            break
        elif guess < random_number:
            print("Too low")
            attemps = attemps - 1
        elif guess > random_number:
            print("Too high")
            attemps = attemps -1
        else:
            print("You put a wrong input, try again.")

    if attemps == 0:
        print(f"You lose. The answer is {random_number}")

elif difficulty == 'hard':
    # Attemps
    attemps = 5
    while attemps > 0:
        print(f"You have {attemps} remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == random_number:
            print(f"Very well. You guessed the number {guess}")
            break
        elif guess < random_number:
            print("Too low")
            attemps = attemps - 1
        elif guess > random_number:
            print("Too high")
            attemps = attemps -1
        else:
            print("You put a wrong input, try again.")
    if attemps == 0:
        print(f"You lose. The answer is {random_number}")

else:
    print("You chose a wrong world try again.")



