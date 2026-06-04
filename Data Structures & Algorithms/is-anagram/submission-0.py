class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_map1 = {}
        for char in s:
            if char in freq_map1:
                freq_map1[char] += 1
            else:
                freq_map1[char] = 1

        freq_map2 = {}
        for char in t:
            if char in freq_map2:
                freq_map2[char] += 1
            else:
                freq_map2[char] = 1
        
        return freq_map1 == freq_map2
        