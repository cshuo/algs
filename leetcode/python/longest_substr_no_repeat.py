class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        Time: O(N), Space: O(N)
        """
        hs = {}
        i = 0
        point = 0
        max_len = 0
        while i < len(s):
            if s[i] in hs.keys() and hs[s[i]] >= point:
                if i - point > max_len:
                    max_len = i - point
                point = hs[s[i]] + 1
            else:
                if i == len(s) - 1 and i - point + 1 > max_len:
                    max_len = i - point + 1
            hs[s[i]] = i
            i += 1
        return max_len
