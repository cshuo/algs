class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        hash = {}
        rt = []
        st = []

        for n in nums:
            while st and st[-1] < n:
                hash[st.pop()] = n
            st.append(n)

        for n in findNums:
            rt.append(hash.get(n, -1))