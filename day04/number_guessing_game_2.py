import random

number = random.randint(1, 20)


while True:
    users_guess = input("Guess a number between 1-20:")
    if users_guess == 'x':
        print("Bye!")
        break
    users_guess = int(users_guess)
    if number > users_guess:
        print("Your guess is smaller than the number in the system")
    elif number < users_guess:
        print("Your guess is bigger than the number in the system")
    elif number == users_guess:
        print("Wow! you right! good job :)")
        break


