class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[-inf]*(target+1) for i in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 0
        for i in range(1,n+1):
            for j in range(1,target+1):
                if j-nums[i-1]>=0:
                    dp[i][j] = max(dp[i-1][j],dp[i-1][j-nums[i-1]]+1)
                else:
                    dp[i][j] = dp[i-1][j]
        if dp[n][target] >= 0:
            return dp[n][target]
        else: return -1