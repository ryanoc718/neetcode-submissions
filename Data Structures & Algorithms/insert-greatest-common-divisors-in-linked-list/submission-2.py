# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first, second = head, head.next
        def gcd(f, s):
            while s:
                f, s = s, f%s
            return f
        while second:
            temp = ListNode(gcd(first.val, second.val), second)
            first.next = temp
            first = second
            second = second.next
        return head