class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 0:
            return s
        head_step = numRows * 2 - 2
        head_s, tail_s = '', ''
        for i in xrange(0, len(s), head_step):
            head_s = ''.join([head_s, s[i]])
        for i in xrange(numRows-1, len(s), head_step):
            tail_s = ''.join([tail_s, s[i]])
        print head_s, tail_s

        mid = ''
        for i in xrange(1, numRows-1):
            l = i
            r = i + 2*(numRows-i) - 2
            while l < len(s) and r < len(s):
                mid = ''.join([mid, s[l], s[r]])
                l += head_step
                r += head_step
            if l < len(s):
                mid = ''.join([mid, s[l]])
            elif r < len(s):
                mid = ''.join([mid, s[r]])
        return ''.join([head_s, mid, tail_s])


if __name__ == '__main__':
    s = Solution()
    print s.convert("PAYPALISHIRING", 3)