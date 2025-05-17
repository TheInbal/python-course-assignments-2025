import random

turn_number = 0

while True:
    turn_number = turn_number + 1
    print(f"Welcome to the number guessing game! \nThis is turn number {turn_number}")

    number = random.randint(1, 20)

    # Debug mode variables:
    debug_val = 0
    debug_mode = 0
    # Move mode variables:
    move_val = 0
    move_mode = 0


    while True:
        if move_mode == 1:
            move_step = random.randint(-2, 2)
            number = number + move_step
        if debug_mode == 1:
            print("The number is: ", number)
        users_guess = input("Guess a number between 1-20:")

        if users_guess == 'n':
            print("OK, let's start again")
            break

        if users_guess == 'm':
            move_val = move_val + 1
            move_mode = move_val % 2
            if move_mode == 1:
                print("Move mode on")
            elif move_mode == 0:
                print("Move mode off")
            continue

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
    continue
