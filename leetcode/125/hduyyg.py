# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/125
# time: O(n)

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        L, R = 0, len(s) - 1
        while L < R:
            while L < R and not s[L].isalnum(): L += 1
            while L < R and not s[R].isalnum(): R -= 1
            if L >= R: break
            if s[L].upper() != s[R].upper(): return False
            L, R = L + 1, R - 1
        return True
