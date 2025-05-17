import random

number = random.randint(1, 20)

debug_val = 0
debug_mode = 0


while True:
    if debug_mode == 1:
        print("The number is: ", number)
    users_guess = input("Guess a number between 1-20:")
    if users_guess == 'd':
        debug_val = debug_val + 1
        debug_mode = debug_val % 2
        if debug_mode == 1:
            print("Debug mode on")
        elif debug_mode == 0:
            print("Debug mode off")
        continue
    if users_guess == 's':
        print(number)
        continue
    elif users_guess == 'x':
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