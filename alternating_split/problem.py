class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second


def push(cursor, node):
    cursor.next = node
    temporary = node.next
    node.next = None
    return node, temporary


def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError()

    head_first = head
    cursor_first = head
    head_second = head.next
    cursor_second = head.next

    head_first.next = None

    state = True
    cursor = head_second.next

    head_second.next = None

    while cursor is not None:
        if state:
            cursor_first, cursor = push(cursor_first, cursor)
        else:
            cursor_second, cursor = push(cursor_second, cursor)

        state = not state

    return Context(head_first, head_second)
