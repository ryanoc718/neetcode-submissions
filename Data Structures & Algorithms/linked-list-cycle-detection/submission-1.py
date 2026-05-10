# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tail = skip = head
        while skip != None:
            if skip.next and skip.next.next:
                skip = skip.next.next
            else:
                return False
            tail = tail.next
            if tail == skip:
                return True
        return False