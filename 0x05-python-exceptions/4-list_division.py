#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    ''' Returns a new list of division result between
    my_list_1 and my_list_2

    >>> list_division([10, 8, 4], [2, 4, 4])
    [5.0, 2.0, 1.0]
    >>>  list_division([10, 8, 4, 4], [2, 0, "H", 2, 7])
    division by 0
    wrong type
    out of range
    [5.0, 0, 0, 2.0, 0]

    '''
    new_list = []
    err = []

    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            new_list.append(result)

        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)

        except TypeError:
            print("wrong type")
            new_list.append(0)

        except IndexError:
            print("out of range")
            new_list.append(0)

        finally:
            pass

    return new_list
