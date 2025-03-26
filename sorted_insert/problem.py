"""For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""


def sorted_insert(head, data):
    node = Node(data)
    current = head
    if current is None:
        return node

    if current.data > data:
        node.next = current
        return node

    while current.next is not None and current.next.data < data:
        current = current.next

    node.next = current.next
    current.next = node
    return head
