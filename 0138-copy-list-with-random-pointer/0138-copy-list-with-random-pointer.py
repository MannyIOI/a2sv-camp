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
        curr = head
        randomIndexes = []
        elements = []
        
        while curr:
            randIndex = 0
            randElement = head
            while randElement:
                if curr.random == None:
                    randomIndexes.append(None)
                    break

                if randElement == curr.random:
                    randomIndexes.append(randIndex)
                
                randIndex += 1
                randElement = randElement.next
                
            elements.append(curr.val)
            curr = curr.next
            
        newNodes = [Node(element) for element in elements]
        newNodes += [None]
        
        for i in range(len(newNodes) - 1):
            newNodes[i].next = newNodes[i + 1]
            if randomIndexes[i] != None:
                newNodes[i].random = newNodes[randomIndexes[i]]
        
        return newNodes[0]
                
                
                
                
        