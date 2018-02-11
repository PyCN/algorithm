# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/112
# time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.find_path_sum(root, count=0, target=sum)

    def find_path_sum(self, root, count, target):
        if root is None: return False
        count += root.val
        if root.left is None and root.right is None:
            return True if count == target else False
        if self.find_path_sum(root.left, count, target): return True
        if self.find_path_sum(root.right, count, target): return True
        return False
