def loop_size(node):
    slow = node
    fast = node
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return 0

    count = 1
    fast = fast.next
    while fast != slow:
        count += 1
        fast = fast.next

    return count
