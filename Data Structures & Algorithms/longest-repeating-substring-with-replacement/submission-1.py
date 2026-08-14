class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Input: s = "XYYX", k = 2
                    |
                     |
        
        max_s, arr_len, temp_s
        1. left and right, 0, 1
        2. while r is less than arr_len
        3. Find the most frequent character of the substring
        4. Substract substring length from most frequent
        5. That is the number of replacements
        6. check if its less or equal than k 
        7. If yes, update max_s and r +=1
        8. If not l-=1
        '''
        max_s = 0
        arr_len = len(s)
        count = {}
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)

            if (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l+=1

            max_s = max(max_s, r-l+1)

        return max_s
             
