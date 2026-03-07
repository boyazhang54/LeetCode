class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        comp_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in comp_map:
                return [comp_map[complement], i]
            comp_map[complement] = i