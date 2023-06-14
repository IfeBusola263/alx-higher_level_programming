#!/usr/bin/python3
def search_replace(my_list, search, replace):
    ''' Replaces the item 'search' in the list 'my_list'
    with new element 'replace'

    >>> search_replace([1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89], 2, 89)
    [1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]

    '''

    # Create a new list
    new_list = []

    # loop throught the list to comapre items
    for item in range(len(my_list)):
        if my_list[item] == search:

            # if the comparism is true then replace
            new_list.append(replace)

        # otherwise if in the element in the new list
        else:
            new_list.append(my_list[item])

    return new_list
