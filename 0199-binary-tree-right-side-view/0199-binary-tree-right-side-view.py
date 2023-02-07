# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightSide = []
        
        queue = collections.deque([(root, 0)])
        
        while queue:
            node, level = queue.popleft()

            if not node:
                continue

            if level == len(rightSide):
                rightSide.append(node.val)
            
            queue.append((node.right, level + 1))
            queue.append((node.left, level + 1))
        
        return rightSide