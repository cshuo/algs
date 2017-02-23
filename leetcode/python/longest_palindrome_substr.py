class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def isPalin(s, bg, end):
            if bg < 0: return False
            while bg < end:
                if s[bg] != s[end]: return False
                bg += 1
                end -= 1
            return True

        max_len = 0
        palin = ""
        for i in xrange(len(s)):
            if isPalin(s, i-max_len-1, i):
                palin = s[i-max_len-1:i+1]
                max_len += 2
            elif isPalin(s, i-max_len, i):
                palin = s[i-max_len:i+1]
                max_len += 1
        return palin

if __name__ == '__main__':
    s = Solution()
    print s.longestPalindrome("aab")
