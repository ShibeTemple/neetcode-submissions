class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        # DFS
        def dfs(r, c):
            # out of bounds check
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                # visited water
                grid[r][c] == "0"
            ):
                return

            grid[r][c] = "0" # ERASES FROM THE GRID.

            # check each immediate neighbor. (up down left right)
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # CORE LOOP
        for r in range(ROWS):
            for c in range(COLS):
                # if cell has land
                if grid[r][c] == "1":
                    # remove the entire thing from the map
                    dfs(r, c)
                    # increase island count
                    islands += 1

        return islands