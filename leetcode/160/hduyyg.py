# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/160
# time: O(n)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None: return None
        lengthA = self.get_length(headA)
        lengthB = self.get_length(headB)
        if lengthA < lengthB:
            for i in range(lengthA, lengthB): headB = headB.next
        else:
            for i in range(lengthB, lengthA): headA = headA.next
        while headA is not None and headB is not None:
            if headA == headB: return headA
            headA, headB = headA.next, headB.next
        return None

    def get_length(self, head):
        if head is None: return 0
        p, length = head, 0
        while p: length, p = length + 1, p.next
        return length
