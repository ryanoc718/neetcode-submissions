# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = cur = ListNode()
        while cur:
            minNode = None
            minI = -1
            for i, node in enumerate(lists):
                if node and (not minNode or minNode.val > node.val):
                    minNode = node
                    minI = i
            cur.next = minNode
            cur = minNode
            if minNode:
                lists[minI] = lists[minI].next
        return dummy.next