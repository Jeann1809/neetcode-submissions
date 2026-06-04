class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        Input: s = "tab a cat"
                    |
                            |
        Left and right pointers
        While left < right
        Check if left isalpha if not move right
        Check if right isalpha if not move left
        Check if char.lower() de left y right son iguales
            If yes, move left right and right left
            If no, return false 
        Output: false

        '''
        l = 0
        r = len(s)-1

        while l < r:
            if not s[l].isalnum():
                l+=1
                continue
            if not s[r].isalnum():
                r-=1
                continue

            if s[l].lower() == s[r].lower():
                l+=1
                r-=1
            else:
                return False
        return True

        