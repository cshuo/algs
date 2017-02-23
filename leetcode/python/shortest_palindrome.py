# coding:utf-8
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        j = 0
        for i in xrange(len(s)-1, -1, -1):
            if s[i] == s[j]:
                j+= 1
        # j之后的元素必不可能在现存的回文串中
        if j == len(s):
            return s

        return ''.join([s[len(s)-1:j-1:-1], self.shortestPalindrome(s[:j]), s[j:]])

"""
启发: 解决思路可从反方向思考，如本例对于找当前字符串中的回文串，反向思考就是先排除所有不可能存在当前回文串中的字符，
(利用回文串的必要条件即可)，从而降低问题的时间复杂度。
"""

if __name__ == '__main__':
    s = Solution()
    print s.shortestPalindrome("asdf")
