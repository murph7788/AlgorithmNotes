"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        import heapq

        if not lists:
            return None

        min_heap = []
        for head in lists:
            if head:
                heapq.heappush(min_heap, (head.val, head))

        dummy = ListNode()
        cur = dummy
        while min_heap:
            cur.next = heapq.heappop(min_heap)[1]
            cur = cur.next
            if cur.next:
                heapq.heappush(min_heap, (cur.next.val, cur.next))

        return dummy.next
