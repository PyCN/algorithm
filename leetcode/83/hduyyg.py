# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/83
# time: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return head
        flag, cur, tail = [], head, head.next
        while tail:
            if tail.val != cur.val:
                cur.next = tail
                cur = tail
            tail = tail.next
        cur.next = tail
        return head
