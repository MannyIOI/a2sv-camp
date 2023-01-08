"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import random
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        bridge = {None: None}
        
        curr = head
        while curr:
            copy = Node(curr.val)
            bridge[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            bridge[curr].next = bridge[curr.next]
            bridge[curr].random = bridge[curr.random]
            curr = curr.next
        
        return bridge[head]
            
        
        
                
                
                
                
        