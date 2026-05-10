"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        curr = head.next
        headNode = Node(head.val)
        temp = headNode
        nodes = {}
        nodes[head] = headNode
        while curr:
            temp.next = Node(curr.val)
            temp = temp.next
            nodes[curr] = temp
            curr = curr.next
        temp.next = None
        curr = head
        temp = headNode
        while curr:
            nodes[curr].random = None if not curr.random else nodes[curr.random]
            curr = curr.next
            temp = temp.next
        return headNode

            
            

    