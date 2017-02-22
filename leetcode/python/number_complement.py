class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        tmp_num = num
        bit_num = 0
        while tmp_num > 0:
            bit_num += 1
            tmp_num /= 2
        import math
        return int(math.pow(2, bit_num) - 1 - num)

