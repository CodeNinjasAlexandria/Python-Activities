import random

number_to_guess = random.randint(1, 10)
user_guess = int(input("Guess a number between 1 and 10: "))

if user_guess == number_to_guess:
    print("Well done! You guessed right!")
else:
    print("Sorry, that's wrong. The correct number was " + str(number_to_guess) + ".")