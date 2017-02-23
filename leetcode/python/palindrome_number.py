class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        if not len(x): return False
        bg, end = 0, len(x) - 1
        while bg < end:
            if x[bg] != x[end]: return False
            bg += 1
            end -= 1
        return True

    def reverseHalfSlt(self, x):
        if x < 0 or (x and x % 10 == 0): return False
        r_x = 0
        while x > r_x:
            r_x = x % 10 + r_x * 10
            x /= 10
        return r_x == x or r_x / 10 == x


if __name__ == '__main__':
    s = Solution()
    print s.isPalindrome("a")
    print s.reverseHalfSlt(0)
