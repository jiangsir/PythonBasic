# 羅馬數字 轉 整數
##
##


class Solution:
    table = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50,
             'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        i = 0
        while i < len(s):
            if s[i:i+2] == 'IV':
                ans += self.table['IV']
                i += 1
            elif s[i:i+2] == 'IX':
                ans += self.table['IX']
                i += 1
            elif s[i:i+2] == 'XL':
                ans += self.table['XL']
                i += 1
            elif s[i:i+2] == 'XC':
                ans += self.table['XC']
                i += 1
            elif s[i:i+2] == 'CD':
                ans += self.table['CD']
                i += 1
            elif s[i:i+2] == 'CM':
                ans += self.table['CM']
                i += 1
            else:
                ans += self.table[s[i]]

            i += 1

        return int(ans)


s = Solution()

assert 3 == s.romanToInt('III')
assert 4 == s.romanToInt('IV')
assert 5 == s.romanToInt('V')
assert 10 == s.romanToInt('X')

assert 58 == s.romanToInt('LVIII')
assert 1994 == s.romanToInt('MCMXCIV')
assert 10 == s.romanToInt('X')
