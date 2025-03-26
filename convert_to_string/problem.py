def iter_list(node):
    while node is not None:
        yield node.data
        node = node.next

    yield None


def stringify(node):
    return " -> ".join(str(node) for node in iter_list(node))
