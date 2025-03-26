from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next


def get_nth(node, index):
    if index < 0:
        raise IndexError("Index out of range")

    if node is None:
        raise IndexError("Index out of range")

    for _ in range(index):
        node = node.next
        if node is None:
            raise IndexError("Index out of range")

    return node
