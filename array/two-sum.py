class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in comp_map:
                return [comp_map[complement], i]
            comp_map[complement] = i