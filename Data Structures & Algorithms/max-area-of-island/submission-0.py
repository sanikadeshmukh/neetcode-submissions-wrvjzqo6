class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visit.add((r, c))
            area = 1   # ⭐ start counting

            while q:
                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if (nr in range(rows) and
                        nc in range(cols) and
                        grid[nr][nc] == 1 and
                        (nr, nc) not in visit):

                        q.append((nr, nc))
                        visit.add((nr, nc))
                        area += 1   # ⭐ increase area

            return area   # ⭐ return size

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    max_area = max(max_area, bfs(r, c))  # ⭐ take max

        return max_area
        