# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        stack = [root] if root else []
        while stack:
            depth += 1
            queue = []
            for el in stack:
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
            stack = queue
        return depth
