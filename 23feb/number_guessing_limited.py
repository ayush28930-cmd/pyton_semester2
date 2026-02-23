import random

while True:
    number = random.randint(1, 50)
    attempts = 5

    print("\nGuess a number between 1 and 50")
    
    while attempts > 0:
        guess = int(input("Enter guess: "))
        attempts -= 1

        if guess == number:
            print("Correct! You won!")
            break
        elif guess > number:
            print("Too high!")
        else:
            print("Too low!")

        print("Attempts left:", attempts)

    if attempts == 0:
        print("You lost! Number was:", number)

    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        break