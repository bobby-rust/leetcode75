class Solution:

    def extractColumns(self, grid: List[List[int]]) -> Dict:
        '''
        Extracts columns along with their number of occurrences
        '''
        n = len(grid)

        cols = {} 
        for i in range(n):
            cur = []
            for j in range(n):
                cur.append(grid[j][i])
            strcur = str(cur)
            if strcur in cols:
                cols[strcur] += 1
            else:
                cols[strcur] = 1

        return cols

    def equalPairs(self, grid: List[List[int]]) -> int:
        cols = self.extractColumns(grid)
        count = 0
        for row in grid:
            strrow = str(row)
            if strrow in cols:
                count += cols[strrow]

        return count 
