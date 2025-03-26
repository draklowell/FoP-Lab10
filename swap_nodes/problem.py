from preloaded import Node


def swap(node):
    node1, node2 = node, node.next
    if node2 is None:
        return node1, None

    node2.next, node1.next = node1, node2.next
    return node2, node1


def swap_pairs(head):
    if head is None:
        return None

    head, node = swap(head)
    if node is None:
        return head

    prev = node
    while prev is not None:
        node1 = prev.next
        if node1 is None:
            return head

        node1, node2 = swap(node1)
        prev.next = node1
        prev = node2

    return head
