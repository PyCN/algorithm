# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/23
# time: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = ListNode(0)
        new_head.next = head
        self.swap(new_head)
        return new_head.next

    def swap(self, head):
        if head is None or head.next is None or head.next.next is None: return
        node1 = head.next
        node2 = head.next.next
        node1.next = node2.next
        node2.next = node1
        head.next = node2
        self.swap(node1)
