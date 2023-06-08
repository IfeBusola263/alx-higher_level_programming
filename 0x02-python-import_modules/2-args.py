#!/usr/bin/python3

# check if it's the main program
if __name__ == '__main__':
    # Bring in right module for command line args
    import sys

    # check if there no argument
    if len(sys.argv) == 1:
        print("{} arguments.".format(0))

    # check if there's just one argument
    elif len(sys.argv) == 2:
        print("{} argument:".format(1))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))

    # check for more than one argument
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
