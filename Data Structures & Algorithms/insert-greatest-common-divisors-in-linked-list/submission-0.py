# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first, second = head, head.next
        while second:
            gcd = 1
            i = 1
            while i <= min(first.val, second.val):
                if first.val%i == 0 and second.val%i == 0:
                    gcd = i
                i += 1
            temp = ListNode(gcd, second)
            first.next = temp
            first = second
            second = second.next
        return head
                