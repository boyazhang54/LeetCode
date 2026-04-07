class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0]) # n行 m列
        def bfs(i,j):
            ans = 0
            q = deque([(i,j)])
            grid[i][j]=0
            while q:
                x,y = q.popleft()
                d = ((0,1),(0,-1),(1,0),(-1,0))
                for dx,dy in d:
                    if 0<=x+dx<n and 0<=y+dy<m and grid[x+dx][y+dy] == 1:
                        q.append((x+dx,y+dy))
                        grid[x+dx][y+dy] = 0
                ans += 1
            return ans
        res = 0
        for i,row in enumerate(grid):
            for j,e in enumerate(row):
                if e==1:
                    ans = bfs(i,j)
                    res = max(res,ans)
        return(res)