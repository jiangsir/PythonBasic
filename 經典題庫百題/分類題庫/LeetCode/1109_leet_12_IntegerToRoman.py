## 整數轉整數
##
##

class Solution:

    table = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50,
             'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
    

    def searchKey(self, search):
        for key, value in self.table.items():
            if search == value:
                return key
        
    
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        #print('num=', num, end='')
        ans = ''
        for value in sorted(self.table.values(), reverse=True):
            #print(value)
            while num >= value:
                num = num - value
                ans += self.searchKey(value)
                
        #print('ans=', ans)
        return ans
                


s = Solution()
assert 'III' == s.intToRoman(3)
assert 'IV' == s.intToRoman(4)
assert 'V' == s.intToRoman(5)
assert 'MCMXCIV' == s.intToRoman(1994)
assert 'LVIII' == s.intToRoman(58)
assert 'X' == s.intToRoman(10)
assert '' == s.intToRoman(0)

