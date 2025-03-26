class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_duplicates(head):
    pointer1 = head
    pointer2 = head
    while pointer1 is not None:
        pointer2 = pointer1.next
        while pointer2 is not None and pointer1.data == pointer2.data:
            pointer2 = pointer2.next

        pointer1.next = pointer2
        pointer1 = pointer2

    return head
