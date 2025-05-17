import random

number = random.randint(1, 20)
users_guess = int(input("Guess a number between 1-20:"))
if number == users_guess:
    print("Wow! you right! good job :)")
elif number >> users_guess:
    print("Your guess is smaller than the number in the system")
elif number << users_guess:
    print("Your guess is bigger than the number in the system")