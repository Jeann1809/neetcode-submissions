class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #input: s = 'AAABC' k = 1  | count = {A: 0, B: 1, C: 1} | window = 'BC' | res = 4
        # left       |          | len(window) - most_freq <= k
        # right         |
        count = {}
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            most_frequent = max(count.values())
            while (r-l+1) - most_frequent > k:
                count[s[l]] -= 1
                l+=1
            res = max(res, r-l+1)
        return res
            
