#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# python does not handle modulo division gracefully 17 % 10
# check if number of negative
if number < 0:
    neg_num = number
    number = number * -1
    last_digit = number % 10
    if last_digit == 0:
        print(f"Last digit of {neg_num} is {last_digit} and is 0")
    else:
        print(f"Last digit of {neg_num} is {last_digit * -1}\
 and is less than 6 and not 0")
# for positive numbers generated
else:
    last_digit = number % 10
    if last_digit > 5:
        print(f"Last digit of {number} is {last_digit} and is greater than 5")
    elif last_digit == 0:
        print(f"Last digit of {number} is {last_digit} and is 0")
    elif last_digit <= 5 and last_digit != 0:
        print(f"Last digit of {number} is {last_digit}\
 and is less than 6 and not 0")
