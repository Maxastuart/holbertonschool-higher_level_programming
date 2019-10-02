#!/usr/bin/python3
class Node:
    """Define a Node class."""

    def __init__(self, data, next_node=None):
        """Define and initialize a node.
        data (int): the data to store in the node
        next_node (Node): optional, the next node
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if next_node is not None or not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Define data property"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the value of the Node.
        value (int): the new value to store
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Define next_node property"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the value of the next node.
        value (Node): the new next_node to point to
        """
        if value is not None or not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Define a SinglyLinkedList class."""

    def __init__(self):
        """Define and initialize a singly linked list."""
        self.__head = None

    def __str__(self):
        """Define a singly linked list as a string"""
        str_list = ""
        if self.__head:
            str_list += str(self.__head._Node__data)
            temp = self.__head._Node__next_node
            while temp:
                str_list += "\n" + str(temp._Node__data)
                temp = temp._Node__next_node
        return str_list

    @property
    def head(self):
        """Define head property."""
        return self.__head

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list \
        (increasing order).
        value (int): the value to store at the new node in the list
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif value <= self.__head._Node__data:
            new_node._Node__next_node = self.__head
            self.__head = new_node
        elif self.__head._Node__next_node is None:
            self.__head._Node__next_node = new_node
        else:
            temp = self.__head
            while temp._Node__next_node:
                if value <= temp._Node__next_node._Node__data:
                    new_node._Node__next_node = temp._Node__next_node
                    temp._Node__next_node = new_node
                    break
                else:
                    temp = temp._Node__next_node
                    if not temp._Node__next_node:
                        temp._Node__next_node = new_node
                        break
