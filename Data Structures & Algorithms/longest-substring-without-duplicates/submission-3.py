class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        charset = set([])
        max_count = 0
        while r < len(s):
    
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            
            charset.add(s[r])
            max_count = max(max_count, len(charset))
            r+=1
        return max_count
        