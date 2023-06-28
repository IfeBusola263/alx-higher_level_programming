#!/usr/bin/python3
'''This module imitates the singly linked lists in C language'''


class Node:
    '''Class node is makes instantiation of linked lists.'''

    def __init__(self, data, next_node=None):
        '''The init methods runs when an instance of the class
        Node is created and executes the indented block of codes.'''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''Method data is a getter used to protect the parameter
        data(self.data).'''

        return self.__data

    @data.setter
    def data(self, value):
        '''Sets the new value of the parameter data, protecting
        the object from any offensive input.'''

        # Check for correct type
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        '''Method next_node gets the field next_node(self.next_node
        after setter sets the attribute.'''

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''Sets the value of parameter next_node, protecting the
        instance(object) from offensive input.'''

        if type(value) is not Node:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    '''Class singlylinkedlist defines a singly linked list.'''

    def __init__(self):
        '''Runs immediately an instance of the class is created'''
        self.__head = []

    def __str__(self):
        '''Prints a string representation of the object passed to it.'''
        if len(self.__head) > 1:
            for i in range(len(self.__head) - 1):
                print(self.__head[i])
            return str(self.__head[-1])
        else:
            return

    def sorted_insert(self, value):
        '''Creates the list with the elements sorted in increasing order'''
        self.__head.append(value)
        self.__head.sort()
