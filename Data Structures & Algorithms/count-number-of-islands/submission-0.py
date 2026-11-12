class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #depth first search 
        #u can go left right up down 
        #start from top left, if u see the 1 then add the land and change all the 1 on the four sides.. and if its not seeing 1 anymore then go back to (what?) 
        islands = 0 

        row, col = len(grid), len(grid[0]) 

        def dfs(r, c):
            if grid[r][c] == '0':
                return 

            grid[r][c] = '0'
            
            if r-1>=0: dfs(r-1,c) #up 
            if r+1<row: dfs(r+1,c) #down 
            if c-1>=0: dfs(r,c-1) #left 
            if c+1<col: dfs(r,c+1) #right 

        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1': 
                    islands+= 1 
                    dfs(r, c)
        return islands

