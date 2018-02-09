# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/104
# time: O(n)

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
        if root is None: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
