# coding: utf-8

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        doc: Regular Expression Matching
        """
        sg = [[False for i in xrange(len(p) + 1)] for j in xrange(len(s) + 1)]

        sg[0][0] = True

        # p串的前i个能否匹配Null
        for i in xrange(len(p)):
            sg[0][i+1] = p[i] == '*' and sg[0][i-1]

        # dp: 子结构,s[:i]与p[:j]能够匹配, 三种情况.
        for i in xrange(len(s)):
            for j in xrange(len(p)):
                if p[j] == '.' or p[j] == s[i]:
                    sg[i+1][j+1] = sg[i][j]
                elif p[j] == '*':
                    if p[j-1] != s[i] and p[j-1] != '.':
                        sg[i+1][j+1] = sg[i+1][j-1]
                    else:
                        sg[i+1][j+1] = sg[i+1][j] or sg[i][j+1] or sg[i+1][j-1]

        return sg[len(s)][len(p)]


if __name__ == '__main__':
    s = Solution()
    print s.isMatch("bb", ".bab")
