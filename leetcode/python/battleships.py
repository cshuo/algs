class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if board is None or len(board) == 0 or len(board[0]) == 0:
            return 0

        count = 0
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == 'X' and (i==0 or board[i-1][j] == '.') and (j==0 or board[i][j-1] == '.'):
                    count += 1

        return count


if __name__ == '__main__':
    ship = [['.','.','X'],['.','.','X'],['X','X','X']]
    s = Solution()
    print s.countBattleships(ship)

