import random

num_guess = int(input("Give me a number between 1-100.\n"))
random_int = random.randint(0, 101)

if num_guess == random_int:
    print("Wow, that was amazing (with sarcasm). ")
elif num_guess > random_int:
    print("Too high! Guess again!")
elif num_guess < random_int:
    print("Too low! Guess again!") 