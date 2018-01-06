# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/5
# time: O(n)

class Solution:
    def longestPalindrome(self, ss):
        """
        :type s: str
        :rtype: str
        """
        s = '#'.join(['', '#'.join(ss), ''])
        ansid, id, mx, lens = 1, 1, 0, len(s)
        p = [1 for _ in range(lens)]
        for i in range(1, lens):
            if i < mx: p[i] = min(p[2 * id - i], mx - i)
            while p[i] <= i and i + p[i] < lens and s[i + p[i]] == s[i - p[i]]:
                p[i] += 1
            if i + p[i] > mx:
                id, mx = i, i + p[i]
                if p[i] > p[ansid]: ansid = i
        res = ''.join(
        	[s[i] for i in range(ansid - p[ansid] + 2, ansid + p[ansid], 2)])
        return res
