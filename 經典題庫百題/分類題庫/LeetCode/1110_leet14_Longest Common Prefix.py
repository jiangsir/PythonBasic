class Solution:

    def allmatch(self, strs, l):
        prefix = strs[0][0:l]
        for ss in strs:
            if not ss.startswith(prefix):
                return False
        return True
        
    
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        end = 0
        shortest = -1
        for s in strs:
            if shortest==-1 or len(s) < shortest:
                shortest = len(s)
        
        #print(shortest)
            
        for i in range(shortest, 0, -1):
            if self.allmatch(strs, i):
                return strs[0][0:i]
        return ''


s = Solution()
assert 'fl' == s.longestCommonPrefix(["flower","flow","flight"])
assert '' == s.longestCommonPrefix(["dog","racecar","car"])
assert '' == s.longestCommonPrefix(["dog","racecar",""])
assert 'd' == s.longestCommonPrefix(["dog","dacecar","d"])
