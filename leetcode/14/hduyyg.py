# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/14
# time: O(n*m)

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0: return ''
        if len(strs) == 1: return strs[0]
        res = self.get_prefix_common_length(
            strs[0], strs[1], max(len(strs[0]), len(strs[1])))
        for i in range(1, len(strs) - 1):
            res = self.get_prefix_common_length(strs[i], strs[i + 1], res)
            if res == -1: return ''
        return strs[0][:res]

    def get_prefix_common_length(self, s1, s2, max_length):
        max_length = min(max_length, min(len(s1), len(s2)))
        for i in range(max_length):
            if s1[i] != s2[i]: return i
        return max_length
