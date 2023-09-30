#!/usr/bin/python3

class Node:
    def __init__(self, data, next_node=None):
        if isinstance(data, int):
            self.__data = data
        else:
            raise TypeError('data must be an integer')
        if isinstance(next_node, Node) or next_node == None:
            self.__next_node = next_node
        else:
            raise TypeError('next_node must be a Node object')
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, value):
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError('data must be an integer')
    @property
    def next_node(self):
        return self.__next_node
    @next_node.setter
    def next_node(self, value):
        if isinstance(value, Node) or value == None:
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')

class SinglyLinkedList:
    def __init__(self):
        self.__head = None
    def __str__(self):
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
