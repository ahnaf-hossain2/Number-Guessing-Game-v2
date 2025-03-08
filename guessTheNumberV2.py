from random import randint

def main():
    computer = randint(1, 100)
    player = int(input('Enter a number between 1 and 10: '))

    while player != computer:
        if player > computer:
            print("Lower number please! ")
        elif player < computer:
            print("Higher number please! ")
        player = int(input())
    else:
        print("You guessed it right!")

if __name__ == "__main__":
    main()
