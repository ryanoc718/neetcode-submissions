# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        node = head
        while node:
            nodes.append(node)
            node = node.next
        i, j = 0, len(nodes)-1
        while i < j:
            temp = nodes[i].next
            nodes[i].next = nodes[j]
            nodes[j].next = temp
            i += 1
            j -= 1
        nodes[i].next = None
