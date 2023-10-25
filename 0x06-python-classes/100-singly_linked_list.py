#!/usr/bin/python3
"""
This module demonstrates how to use a
sorted singly linked list in python
"""


class Node:
    """
    A node class definition

    Attributes:
        data (int): The node data
        next_node (:obj:`Node`, optional) The next node
    """

    def __init__(self, data, next_node=None) -> None:
        """
        Initialize a new data with its data and next node (can be None)
        Throw errors if data is not integer or next_data is not None and
        not a Node class instance

        Args:
            data (int): The node data
            next_node (:obj:`Node`, optional) The next node
        """
        if (not isinstance(data, int)):
            raise TypeError("data must be an integer")
        elif (
            next_node is not None and
            not isinstance(next_node, self.__class__)
        ):
            raise TypeError("next_node must be a Node object")
        else:
            self.__data = data
            self.__next_node = next_node

    @property
    def data(self):
        """Return the data of the node"""
        return (self.__data)

    @property
    def next_node(self):
        """Return the next node of the current node"""
        return (self.__next_node)

    @data.setter
    def data(self, value):
        """Set a new data for the current node"""
        self.__init__(value, self.next_node)

    @next_node.setter
    def next_node(self, value):
        """Set a new next node for the current node"""
        self.__init__(self.data, value)

    def __repr__(self) -> str:
        """
        String representation of the Node class instance

        Args: None
        Returns: the data of the current node
        """
        return (str(self.data))


class SinglyLinkedList:
    """
    A singly linked list class definition

    Attributes:
        data (any): head of the list
    """

    def __init__(self):
        """
        Initialize a new singly linked list to None

        Args: None
        """
        self.__head: Node = None

    def sorted_insert(self, value):
        """
        Add a new element to list by ascending order

        Args:
            value (any): Data of the new node

        Returns: None
        """
        node = Node(value)
        if (self.__head is None):
            self.__head = node
        else:
            last = self.__head
            insertAtTop = False
            while (last is not None):
                if (node.data <= last.data):
                    insertAtTop = True
                    break
                elif (last.next_node is None):
                    break
                elif (node.data <= last.next_node.data):
                    insertAtTop = False
                    break
                else:
                    last = last.next_node
            if (insertAtTop):
                node.next_node = last
                self.__head = node
            else:
                node.next_node = last.next_node
                last.next_node = node

    def __repr__(self) -> str:
        """
        String representation of the SinglyLinkedList class instance

        Args: None
        Returns: a list of node data, each followed by
            line break character
        """
        temp = []
        last = self.__head
        while (last is not None):
            temp.append(str(last))
            last = last.next_node
        return "\n".join(temp)
