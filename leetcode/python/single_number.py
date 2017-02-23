class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rt = 0
        for n in nums:
            rt ^= n
        return rt

if __name__ == '__main__':
    s = Solution()
    print s.singleNumber([1,2,1,2,3,4,3,5,4])
