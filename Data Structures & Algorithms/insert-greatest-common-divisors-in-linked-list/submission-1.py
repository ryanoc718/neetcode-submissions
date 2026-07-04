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
            a, b = max(first.val, second.val), min(first.val, second.val)
            while b:
                a, b = b, a%b
            gcd = a
            temp = ListNode(gcd, second)
            first.next = temp
            first = second
            second = second.next
        return head
                