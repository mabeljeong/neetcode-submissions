class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #dp -> path coming from right + path coming from down
        #m-1 row is all 1, n-1 col is all 1

        row = [1] * n #made the last row.. 

        for i in range(m-1):
            new_row = [1] * n 

            for j in range(n-2, -1, -1) :  
                new_row[j] = row[j] + new_row[j+1]  

            row = new_row


        return row[0]