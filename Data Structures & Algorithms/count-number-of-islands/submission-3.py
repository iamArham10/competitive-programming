class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        bool_arr_cast = [[False for elem in row] for row in grid]
        islands = 0

        def dfs(i, j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0:
                return

            if grid[i][j] != '1' or bool_arr_cast[i][j]:
                return
            # performing dfs
            bool_arr_cast[i][j] = True
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j-1)
            dfs(i, j+1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and bool_arr_cast[i][j] == False:
                    islands += 1
                    dfs(i, j)
        
        return islands



        