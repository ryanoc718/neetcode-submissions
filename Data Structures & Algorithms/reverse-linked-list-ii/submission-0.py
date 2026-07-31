# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        start, prev = ListNode(), ListNode()
        save = ListNode()
        cur = head
        k = 0
        while k < right:
            k += 1
            if k == left-1:
                save = cur
            if k == left:
                start = cur
            temp = cur.next
            if k >= left:
                cur.next = prev
                prev = cur
            if k == right:
                save.next = cur
            cur = temp
        start.next = cur
        return head if head != start else prev
        
