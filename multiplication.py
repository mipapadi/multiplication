# The following program belongs to mipapadi and it is a classic multiplication game.
# Copyright © 2022 mipapadi.

from time import sleep
from random import shuffle

print("Welcome to multiplication game!")
sleep(1)

while 1:

    while 1:
        number = input(
            "Please give an integer number from 0-10 or press q to quit: ")

        if number.isdigit() == True:
            # If it has only digits
            if isinstance(int(number), int) == True and int(number) >= 0 and int(number) <= 10:
                # If it is integer from 0-10
                break
            else:
                # If it is integer out of range or decimal
                continue
        else:

            if number == "q":
                # If it is exit character
                print("Let's try another time. Goodbye!")
                sleep(0.7)
                exit()
            else:
                # If it is character or character with digits
                continue

    # Randomness
    factors = list(range(11))
    shuffle(factors)

    for n in factors:

        while 1:
            # result will be string
            result = input(f"{n} * {number} = ")

            if result.isdigit() == True:
                # If it has only digits
                if isinstance(int(result), int) == True and int(result) == n*int(number):
                    # If it is integer and at the same time the correct result
                    break
                else:
                    # Wrong result
                    print("Try again!")
                    continue
            else:
                if result == "q":
                    # If it is exit character
                    print("Thank you for your effort. Goodbye!")
                    sleep(0.7)
                    exit()
                else:
                    # If it is character or character with digits
                    print("Please give an integer or q to quit.")
                    continue

    print(
        f"Congratulations! You just completed correctly the multiplication of {number}")
    sleep(0.7)
    descision = input(
        "Do you want to continue with another multiplication? (y/n): ")

    if descision == "n":
        print("Alright. Hope to see you again!")
        sleep(0.7)
        print("Bye :)")
        sleep(0.7)
        break
    else:
        continue
