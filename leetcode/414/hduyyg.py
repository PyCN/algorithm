# author:2632158294@qq.com
# github:https://github.com/PyCN/algorithm/tree/master/leetcode/204
# time: o(n)

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        if len_nums < 3: return max(nums)
        que = [nums[0]]
        
        for i in range(1, len_nums):
            if nums[i] != que[0]:
                que.append(nums[i])
                break

        for j in range(i, len_nums):
            if nums[j] != que[0] and nums[j] != que[1]:
                que.append(nums[j])
                break
        if len(que) < 3: return max(que)

        for k in range(j, len_nums):
            if nums[k] == que[0]: continue
            if nums[k] == que[1]: continue
            if nums[k] == que[2]: continue
            min_index = que.index(min(que))
            if que[min_index] < nums[k]: que[min_index] = nums[k]
        return min(que)
