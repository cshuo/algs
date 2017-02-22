class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min = 0
        sum = 0
        for n in nums:
            sum = n * (sum + 1)
            min = max(min, sum)
        return min
