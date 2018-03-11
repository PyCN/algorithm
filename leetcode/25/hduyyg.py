# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/25
# time: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k < 2: return head
        new_head = ListNode(0)
        new_head.next = head
        self.swap(new_head, k)
        return new_head.next

    def swap(self, head, k):
        tail = head
        for i in range(k):
            tail = tail.next
            if tail is None: return
        self.swap(tail, k)
        self.dfs(head.next, 1, k, head, tail.next)

    def dfs(self, node, index, length, head, tail):
        if index == length:
            head.next = node
            return
        self.dfs(node.next, index + 1, length, head, tail)
        node.next.next = node
        if index == 1: node.next = tail
