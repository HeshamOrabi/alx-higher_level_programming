#!/usr/bin/python3
"""Define classes for a singly-linked list."""


class Node:
    """Represent a node in a singly-linked list."""
    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        Raise:
            TypeError: in case data is not int obj
            TypeError: in case next_node in not Node obj
        """
        if isinstance(data, int):
            self.__data = data
        else:
            raise TypeError('data must be an integer')
        if isinstance(next_node, Node) or next_node is None:
            self.__next_node = next_node
        else:
            raise TypeError('next_node must be a Node object')

    @property
    def data(self):
        """Get/set the data of the Node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Get/set the data of the Node."""
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError('data must be an integer')

    @property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Get/set the next_node of the Node."""
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')


class SinglyLinkedList:
    """Represent a singly-linked list."""
    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        result = ""
        tmp = self.__head
        while tmp:
            if tmp.next_node:
                result += str(tmp.data) + "\n"
            else:
                result += str(tmp.data)
            tmp = tmp.next_node
        return result

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.

        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            value: The new Node to nalue.
        """
        new = Node(value)
        tmp = self.__head
        if tmp is None or tmp.data >= value:
            new.next_node = tmp
            self.__head = new
        else:
            while tmp.next_node is not None and tmp.next_node.data < value:
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new
