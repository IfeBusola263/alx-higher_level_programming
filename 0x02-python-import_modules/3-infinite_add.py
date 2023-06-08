#!/usr/bin/python3

# check if it is the main program
if __name__ == "__main__":

    # bring in the right module for comandline args
    import sys

    # define an accumulator
    accumulator = 0

    # loop through the arguments
    for i in range(1, len(sys.argv)):
        accumulator = accumulator + int(sys.argv[i])

    # output the total sum
    print(accumulator)
