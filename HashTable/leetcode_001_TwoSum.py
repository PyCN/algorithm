#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for index, number in enumerate(nums):
            diff = target - number
            if diff in nums_dict:
                return nums_dict[diff], index
            nums_dict[number] = index

        # no special case handling becasue it's assumed that it has only one solution


"""
[1,2]
3
[3,2,4]
6
"""
