#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# check number with specific conditions
# check if the number is positive, print number and is positive
if number > 0:
    print(f"{number} is positive")
# check if the number is zero, print number and is zero
elif number == 0:
    print(f"{number} is zero")
# check if the number is negative, print number and is negative
else:
    print(f"{number} is negative")
