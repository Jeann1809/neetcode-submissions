class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {} # mapping charCount to list of Anagrams
        for string in strs:
            sorted_s_list = sorted(string)
            sorted_s = ''.join(sorted_s_list)

            if sorted_s in hash_map:
                hash_map[sorted_s].append(string)
            else:
                hash_map[sorted_s] = [string]
        
        res = []
        for anagram in hash_map:
            res.append(hash_map[anagram])
        return res
            

        