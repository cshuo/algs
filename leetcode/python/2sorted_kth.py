def findk(nums1, l1, nums2, l2, k):
    if l1 > l2:
        return findk(nums2, l2, nums1, l1, k)
    elif l1 == 0:
        return nums2[k - 1]
    elif k == 1:
        return min(nums1[0], nums2[0])

    i, j = min(l1, k / 2), min(l2, k / 2)
    if nums1[i - 1] > nums2[j - 1]:
        return findk(nums1, l1, nums2[j:], l2 - j, k - j)
    else:
        return findk(nums1[i:], l1 - i, nums2, l2, k - i)


if __name__ == '__main__':
    a = [2, 5, 9]
    b = [1, 3, 4]
    print findk(a, len(a), b, len(b), 6)
