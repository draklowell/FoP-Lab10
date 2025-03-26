class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


def reverse(head):
    def _reverse(node):
        if node.next is None:
            return node, node

        head, tail = _reverse(node.next)
        tail.next = node
        node.next = None
        return head, node

    if head is None:
        return None

    return _reverse(head)[0]
