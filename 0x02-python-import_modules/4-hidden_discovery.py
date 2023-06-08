#!/usr/bin/python3

# check if this is the main program
if __name__ == "__main__":

    # bring in the specified module
    import hidden_4

    # save the variable names in the module in a variable
    content = dir(hidden_4)

    # loop through the list, omitting functions with '_'
    for i in range(len(content)):
        if content[i][0] != '_' and content[i][1] != '_':
            print(content[i])
