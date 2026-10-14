secret = 50

while True:

    guess = int(input("Guess the number: "))

    if guess == secret:
        print("Correct Guess!")
        break

    elif guess > secret:
        print("Too High")

    else:
        print("Too Low")