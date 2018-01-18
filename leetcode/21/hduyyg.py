# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/21
# time: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None: return l2
        if l2 is None: return l1
        head = ListNode(0)
        tail = head
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                tail.next = ListNode(l1.val)
                l1 = l1.next
            else:
                tail.next = ListNode(l2.val)
                l2 = l2.next
            tail = tail.next
        if l1 is None: tail.next = l2
        if l2 is None: tail.next = l1
        return head.next
