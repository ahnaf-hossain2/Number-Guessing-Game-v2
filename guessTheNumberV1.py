from random import randint

def main():
    print("Welcome to the Number Guessing Game!")
    print("In this game, you have to guess a number between 1 to 100.")
    print("If you guess the correct number, you win!")
    while True:
        guessNumber = int(input("Enter any number between 1 to 100: "))
        randomNumber = randint(1, 100)
        if (guessNumber == randomNumber):
            print("You won!")
            break
        else:
            print(f"You lost! The correct number was {randomNumber}")
        again = input("Do you want to try again? (y/n): ")
        if (again == "y" or again == "Y"):
            print("Starting.....")
        elif (again == "n" or again == "N"):
            print("The game is over Give up on your dreams and 死ぬ! ")
            break

if __name__ == "__main__":
    main()
