# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/23
# time: O(nlogk)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(0)
        tail, heap = head, []
        for i in range(len(lists)):
            if lists[i] is not None:
                heapq.heappush(heap, (lists[i].val, i))
        while heap:
            val = heapq.heappop(heap)
            tail.next = ListNode(val[0])
            tail = tail.next
            if lists[val[1]].next is not None:
                lists[val[1]] = lists[val[1]].next
                heapq.heappush(heap, (lists[val[1]].val, val[1]))
        return head.next
