## 回文, 迴文
##
##

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        return x == x[::-1]

s = Solution()

assert True == s.isPalindrome(121) 
assert False == s.isPalindrome(-121) 
assert False == s.isPalindrome(10) 
