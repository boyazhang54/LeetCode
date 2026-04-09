class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        record = [[0]*2 for _ in range (n+1)] # 从1开始计数
        for i in range(1,n+1):
            record[i][0] = max(record[i-1][0], record[i-1][1])
            record[i][1] = record[i-1][0]+ nums[i-1]
        return max(record[n][0],record[n][1])