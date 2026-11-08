class Solution(object):
    def countServers(self, grid):
        m = len(grid)   # 4
        n = len(grid[0])   #  4

        row_count = [0] * m    #   [0, 0, 0, 0]   
        col_count = [0] * n    #   [0, 0, 0, 0]

        # Count servers in each row and column
        for i in range(m):  # 4
            for j in range(n): # 4
                if grid[i][j] == 1:  
                    row_count[i] += 1
                    col_count[j] += 1

        # Count communicating servers
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if row_count[i] > 1 or col_count[j] > 1:
                        count += 1

        return count
