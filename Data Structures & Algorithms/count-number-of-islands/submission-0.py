from collections import deque
class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:

    visited = set()
    islands = 0
    directions = [(1,0),(0,1),(-1,0),(0,-1)]

    for row in range(len(grid)):
      for col in range(len(grid[0])):
        if grid[row][col] == '1' and (row,col) not in visited:
          islands += 1

          #Queue
          q = deque([(row,col)])

          #BFS
          while q:
            i, j = q.popleft()
            visited.add((i,j))
            for di, dj in directions:
              ni , nj = i+di , j+dj

              if ni >= len(grid) or nj >= len(grid[0]) or ni<0 or nj<0:
                continue

              if (ni,nj) not in visited and grid[ni][nj]=='1':
                q.append((ni,nj))
                
    return islands
          


