class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Iterate through strs and order each of the strs
        Iterate again and append them to a hashmap
        Create an array that uses the hashmap info
        '''
        hashmap = {}
        for str in strs:
            ordered_s = ''.join(sorted(str))
            if ordered_s in hashmap:
                hashmap[ordered_s].append(str)
            else:
                hashmap[ordered_s] = [str]
        
        res = []
        for val in hashmap:
            res.append(hashmap[val])
        return res
        