class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # input : s = 'rats' t = 'star' 
        # freq_map = {r: 1, a:1, t:1, s:1}
        freq_map1 = {}
        freq_map2 = {}

        for char in s:
            freq_map1[char] = freq_map1.get(char, 0) + 1
        for char in t:
            freq_map2[char] = freq_map2.get(char, 0) + 1

        return freq_map1 == freq_map2
        

        