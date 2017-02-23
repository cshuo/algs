class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        sign = 0
        leading_len = 0
        str = str.strip()
        while len(str):
            if leading_len > 1:
                return 0
            if str[0].isdigit():
                break
            else:
                leading_len += 1
                if str[0] == '+':
                    sign = 0
                    str = str[1:]
                elif str[0] == '-':
                    str = str[1:]
                    sign = 1

        if not len(str):
            return 0

        end_sign = 0
        while end_sign < len(str) and str[end_sign].isdigit():
            end_sign += 1

        rt = int(str[:end_sign])
        if sign:
            return -(rt>0x80000000 and 0x80000000 or rt)
        else:
            return rt>0x7fffffff and 0x7fffffff or rt

if __name__ == '__main__':
    s = Solution()
    print s.myAtoi("12343423898989")
