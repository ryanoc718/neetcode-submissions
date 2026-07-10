# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(f, s):
            while s:
                f, s = s, f%s
            return f
        a, b = head, head.next
        while b:
            temp = ListNode(gcd(a.val, b.val), b)
            a.next = temp
            a = b
            b = b.next
        return head