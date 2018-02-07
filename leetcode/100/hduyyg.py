# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/100
# time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        flag = self.dfs(p, q)
        return flag

    def dfs(self, tree1, tree2):
        if tree1 is None and tree2 is None: return True
        if tree1 is None or tree2 is None: return False
        if tree1.val != tree2.val: return False
        flag_left = self.dfs(tree1.left, tree2.left)
        flag_right = self.dfs(tree1.right, tree2.right)
        return flag_left and flag_right
