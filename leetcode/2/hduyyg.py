# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# author:2632158294@qq.com
# github:pyCN/algorithm/leetcode/2
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        self.add(l1, l2, 0, res)
        return res.next

    def add(self, l1, l2, last, res):
        if l1 is None and l2 is None:
            res.next = ListNode(last) if last != 0 else None
            return
        
        if l1 is None:
            node = ListNode(l2.val + last)
            l2 = l2.next
        elif l2 is None:
            node = ListNode(l1.val + last)
            l1 = l1.next
        else:
            node = ListNode(l1.val + l2.val + last)
            l1, l2 = l1.next, l2.next

        last = node.val // 10
        node.val %= 10
        self.add(l1, l2, last, node)
        res.next = node
