# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/19
# time: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        res = self.dfs(head.next, n)
        if not isinstance(res, int):
            head.next = res
        elif res + 1 == n:
            head = head.next
        else:
            pass
        return head

    def dfs(self, head, n):
        if head is None: return 0
        res = self.dfs(head.next, n)
        if res is None or not isinstance(res, int):
            head.next = res
            return n
        res += 1
        return res if res != n else head.next
