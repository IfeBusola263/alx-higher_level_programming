#!/usr/bin/python3

# check if this is the main program
if __name__ == "__main__":

    # Load the right modules
    import sys
    from calculator_1 import add, sub, mul, div

    # check for the number of arguments
    if len(sys.argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)

    # check for operator and evaluate expression
    if sys.argv[2] not in '+-*/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        first = int(sys.argv[1])
        second = int(sys.argv[3])
        if sys.argv[2] == '+':
            print("{} + {} = {}".format(first, second, add(first, second)))
        elif sys.argv[2] == '-':
            print("{} - {} = {}".format(first, second, sub(first, second)))
        elif sys.argv[2] == '*':
            print("{} * {} = {}".format(first, second, mul(first, second)))
        else:
            print("{} / {} = {}".format(first, second, div(first, second)))
