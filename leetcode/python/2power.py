def isPowerOf2(num):
    return num & (num - 1) == 0 and num > 0
