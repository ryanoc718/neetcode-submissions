# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            curr1, curr2 = list1, list2
            curr2 = list2
        else:
            curr1, curr2 = list2, list1
        head = curr1
        while curr1 and curr2:
            if not curr1.next:
                curr1.next = curr2
                break
            elif curr1.next.val <= curr2.val:
                curr1 = curr1.next
            else:
                temp = curr1.next
                curr1.next = curr2
                temp2 = curr2.next
                curr2.next = temp
                curr1 = curr2
                curr2 = temp2

        return head