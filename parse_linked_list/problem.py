def linked_list_from_string(s):
    s = [int(i) for i in s.split(" -> ")[:-1]]
    if len(s) == 0:
        return None

    head = Node(s[0])
    current = head
    for i in s[1:]:
        node = Node(i)
        current.next = node
        current = node

    return head
