class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])
        pmt = 0
        for i in xrange(n):
            for k in xrange(m):
                if grid[i][k]:
                    pmt += 4
                    if k < m - 1 and grid[i][k+1]:
                        pmt -= 2
                    if i < n - 1 and grid[i+1][k]:
                        pmt -= 2
        return pmt