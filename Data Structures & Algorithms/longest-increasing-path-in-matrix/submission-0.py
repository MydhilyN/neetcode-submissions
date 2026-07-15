class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS,COLUMNS=len(matrix),len(matrix[0])
        dp={}
        def dfs(r,c,prevval):
            if r<0 or r==ROWS or matrix[r][c]<=prevval or c<0 or c==COLUMNS:
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            res=1
            res=max(res,1+dp(r-1,c,matrix[r][c]))
            res=max(res,1+dp(r+1,c,matrix[r][c]))
            res=max(res,1+dp(r,c+1,matrix[r][c]))
            res=max(res,1+dp(r,c-1,matrix[r][c]))
            dp[(r,c)]=res
            return res
        for r in range(ROWS):
            for c in range(COLUMNS):
                dfs(r,c,-1)
        return max(dp.values())






        