class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        results = []
        rows = ["qwertyuiop","asdfghjkl","zxcvbnm"]
        row_dic = {}
        for i in xrange(3):
            for w in rows[i]:
                row_dic[w] = i
        for w in words:
            row = row_dic[w.lower()[0]]
            in_row = 1
            for c in w.lower():
                if row_dic[c] != row:
                    in_row = 0
                    break
            if in_row:
                results.append(w)
        return results

