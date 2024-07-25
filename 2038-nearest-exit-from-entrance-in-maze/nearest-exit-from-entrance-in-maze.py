from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        x_enter = entrance[0]
        y_enter = entrance[1]

        if maze[x_enter][y_enter] == '+':
            return -1
        
        queue = deque([(x_enter, y_enter, 0)])

        m = len(maze)
        n = len(maze[0])

        seen = {(x_enter, y_enter)}
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def is_exit(x,y):
            return (x==0 or x==m-1 or y==0 or y==n-1) and (x_enter, y_enter) != (x, y)

        def is_valid(x, y):
            return 0<=x<m and 0<=y<n

        while queue:
            x, y, steps = queue.popleft()

            if is_exit(x, y) and maze[x][y]=='.':
                return steps
            
            for dx, dy in directions:
                row = x + dx
                col = y + dy
                if (row, col) not in seen and is_valid(row,col) and maze[row][col]=='.':
                    seen.add((row,col))
                    queue.append((row, col, steps+1))
        
        return -1
            
        