class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        def sorted_insct(l1, l2):
            rt = []
            i, j = 0, 0
            while i < len(l1) and j < len(l2):
                if l1[i] == l2[j]:
                    rt.append(l1[i])
                    i, j = i + 1, j + 1
                elif l1[i] < l2[j]:
                    i += 1
                else:
                    j += 1
            return rt

        return list(set(sorted_insct(sorted(nums1), sorted(nums2))))
