from random import randint

def main():
    computer = randint(1, 100)
    player = int(input('Enter a number between 1 and 10: '))

    guesses = 0
    while player != computer:
        if player > computer:
            print("Lower number please! ")
            guesses += 1
        elif player < computer:
            print("Higher number please! ")
            guesses += 1
        player = int(input('Enter a number between 1 and 100: '))
    else:
        print("You guessed it right in {} attempts!".format(guesses))

if __name__ == "__main__":
    main()
