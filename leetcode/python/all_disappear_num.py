class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in xrange(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])

        return [i+1 for i in xrange(len(nums)) if nums[i] > 0]


if __name__ == '__main__':
    a = [4, 3, 2, 7, 8, 2, 3, 1]
    s = Solution()
    print s.findDisappearedNumbers(a)
