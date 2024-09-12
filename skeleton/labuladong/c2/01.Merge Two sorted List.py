"""
class Node:
    def __init__(self, val=0, next=None)
        self.val = val
        self.next = next
"""


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        head = Node()
        cur = head
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2

            cur = cur.next

        while l1:
            cur.next = l1
            l1 = l1.next

        while l2:
            cur.next = l2
            l2 = l2.next

        return head.next
