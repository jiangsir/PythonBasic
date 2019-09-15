

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 2**31-1 or x < -2**31:
            return 0
        x = str(x)
        if x[0] == '-':
            x = x[::-1]
            rx = 0-int(x[:-1])
            if rx > 2**31-1 or rx < -2**31:
                return 0
            else:
                return rx
        else:
            x = int(x[::-1])
            if x > 2**31-1 or x < -2**31:
                return 0
            else:
                return x


s = Solution()

assert -321 == s.reverse(-123), "錯誤"
assert 21 == s.reverse(120), "錯誤"
assert 0 == s.reverse(1534236469), "錯誤"
