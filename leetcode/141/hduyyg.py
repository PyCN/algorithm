# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/141
# time: O(n)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None: return False
        slow, fast = head, head.next
        while slow != fast:
            if fast is None or fast.next is None: return False
            slow, fast = slow.next, fast.next.next
        return True
