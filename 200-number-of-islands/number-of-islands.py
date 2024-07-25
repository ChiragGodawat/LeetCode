class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        seen = set()

        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        ans = 0

        def is_valid(row, col):
            return 0<=row<m and 0<=col<n

        def dfs(row, col):
            for dx, dy in directions:
                x = row + dx
                y = col + dy

                if (x, y) not in seen and is_valid(x, y) and grid[x][y]=="1":
                    seen.add((x, y))
                    dfs(x,y)


        for i in range(m):
            for j in range(n):
                if (i, j) not in seen and grid[i][j]=="1":
                    seen.add((i, j))
                    ans = ans + 1
                    dfs(i, j)
        
        return ans