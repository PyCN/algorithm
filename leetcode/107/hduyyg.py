# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/107

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: return []
        res = [[root.val]]
        self.dfs(root.left, res, 1)
        self.dfs(root.right, res, 1)
        res.reverse()
        return res

    def dfs(self, root, res, dep):
        if root is None: return
        if dep == len(res): res.append([])
        res[dep].append(root.val)
        self.dfs(root.left, res, dep + 1)
        self.dfs(root.right, res, dep + 1)
