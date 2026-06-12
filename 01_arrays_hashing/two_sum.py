class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d_nums = {}
        for i, current in enumerate(nums):
            complement = target - current
            if complement in d_nums:
                return [i, d_nums[complement]]
            d_nums[current] = i
