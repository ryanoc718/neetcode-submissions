# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        start = head
        slow = prev
        while slow and start and slow != start:
            temp = start.next
            start.next = slow
            temp2 = slow.next
            slow.next = temp
            slow = temp2
            start = temp
        start.next = None
