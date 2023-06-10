#!/Usr/bin/python3
def delete_at(my_list=[], idx=0):
    ''' List -> None
    Mutate the list 'my_list' deleting the item at index 'idx'.
    if index idx is negative or out of range, do nothing

    >>> delete_at([1, 2, 3, 4, 5], 3)
    [1, 2, 3, 5]
    >>> delete_at([1, 2, 3, 4, 5], -3)
    [1, 2, 3, 4, 5]
    >>> delete_at([1, 2, 3, 4, 5], 10)
    [1, 2, 3, 4, 5]

    '''

    highest_index = len(my_list) - 1
    # Check if it's not an empty list
    if my_list is not None:
        if idx >= and idx <= highest_index:

            # remove the item at the specified index
            del my_list[idx]

            # return the modified list
            return my_list
        else:
            return my_list

    # return None if the list is empty
    else:
        return
