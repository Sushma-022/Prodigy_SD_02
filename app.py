import random
generated_number = random.randint(1, 100)
attempts = 0
guess_number = 0

while generated_number != guess_number:
    guess_number = int(input("Enter the number you are guessing:"))
    attempts = attempts + 1

    if guess_number < generated_number:
        print("The guessed number is too low")

    elif guess_number > generated_number:
        print("The guessed number is too high")


    else:
        print(f"The guessed number {guess_number} is correct")
