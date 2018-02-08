# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/101
# time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None: return True
        return self.dfs(root.left, root.right)

    def dfs(self, root1, root2):
        if root1 is None and root2 is None: return True
        if root1 is None or root2 is None: return False
        if root1.val != root2.val: return False
        flag1 = self.dfs(root1.left, root2.right)
        flag2 = self.dfs(root1.right, root2.left)
        return True if flag1 and flag2 else False
