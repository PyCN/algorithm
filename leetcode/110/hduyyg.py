# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/110
# time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return True if self.get_depth(root) >= 0 else False
    
    def get_depth(self, root):
        if not root: return 0
        depth_left = self.get_depth(root.left)
        if depth_left < 0: return -1
        depth_right = self.get_depth(root.right)
        if depth_right < 0: return -1
        if abs(depth_right - depth_left) > 1: return -1
        return max(depth_left, depth_right) + 1
