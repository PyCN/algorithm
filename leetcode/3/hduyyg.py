# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/3
# time: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        flag, length = {}, len(s)
        p, res = 0, 0
        for i in range(length):
            if s[i] not in flag:
                flag[s[i]] = True
            elif flag[s[i]]:
                while s[p] != s[i]:
                    flag[s[p]] = False
                    p += 1
                p += 1
            else:
                flag[s[i]] = True
            res = max(res, i - p + 1)
        return res

