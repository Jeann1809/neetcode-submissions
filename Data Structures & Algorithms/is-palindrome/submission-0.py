class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(' ', '')
        for char in s:
            if char.isalnum():
                continue
            s = s.replace(char,'')

        s_reversed = s[::-1]
        
        return s == s_reversed
        