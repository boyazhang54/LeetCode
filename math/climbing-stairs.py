from functools import *
class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(maxsize = None)
        def dfs(i):   
            return 1 if i==0 or i==1 else dfs(i-1)+dfs(i-2)
        return dfs(n)