#!/usr/bin/python3
from add_0 import add as ad

if __name__ == "__main__":
    import sys
    if sys.argv(0) == "__import__":
        pass
    else:
        a = 1
        b = 2
        print("{} + {} = {}".format(a, b, ad(a, b)))
