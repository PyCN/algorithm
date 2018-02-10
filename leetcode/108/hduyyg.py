# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/108
# time: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: return None
        root = self.get_root(nums, 0, len(nums) - 1)
        return root

    def get_root(self, nums, L, R):
        if L > R: return None
        mid = (L + R + 1) // 2
        root = TreeNode(nums[mid])
        root.left = self.get_root(nums, L, mid - 1)
        root.right = self.get_root(nums, mid + 1, R)
        return root