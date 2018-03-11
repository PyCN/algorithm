# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/28
# time: O(n*m)


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len_needle = len(needle)
        for i in range(len(haystack) - len_needle + 1):
            flag = True
            for j in range(len_needle):
                if haystack[i + j] != needle[j]:
                    flag = False
                    break
            if flag: return i
        return -1