# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level_array = []
        curr_level = -1
        avg_array = [] 
        
        queue = collections.deque([(root, 0)])
        
        while queue:
            node, level = queue.popleft()
            
            if level > curr_level and level_array:
                avg_array.append(sum(level_array) / len(level_array))
                curr_level = level
                level_array = [node.val]
            else:
                level_array.append(node.val)
            
            
            if node.left:
                queue.append((node.left, level + 1))
            
            if node.right:
                queue.append((node.right, level + 1))
        
        avg_array.append(sum(level_array) / len(level_array))
        
        return avg_array