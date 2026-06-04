class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #input: s = 'abccd' output = 3
        #               ||
        # charSet = 'c,d' max_count = 3
        charSet = set()
        max_count = 0
        left = 0
        for right in range(len(s)):
            while s[right] in charSet: 
                charSet.remove(s[left])
                left+=1
            charSet.add(s[right])
            right+=1
            max_count = max(max_count,len(charSet))
        return max_count
