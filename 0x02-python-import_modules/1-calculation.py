#!/usr/bin/python3
# Ensure program runs only when it is the main program
if __name__ == "__main__":

    # move module to source code
    from calculator_1 import add, sub, mul, div

    # initialize the variables
    a = 10
    b = 5

    # display the operations for each module
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
