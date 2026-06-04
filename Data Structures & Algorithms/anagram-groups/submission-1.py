class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # input: [s,s,s,f,f,g,s,g] 
        # output: [[s,s,s,s],[f,f],[g,g]]
        # freq_map = {s: s s s s, f: f f, g: g g}
        freq_map = {}
        strs_len = len(strs)
        sorted_array = [ '' for _ in range(strs_len) ]
        res = []

        for i in range(strs_len):
            sorted_array[i] = ''.join(sorted(strs[i]))

        for i in range(strs_len):
            sorted_string = sorted_array[i]
            original_string = strs[i]

            if sorted_string in freq_map:
                freq_map[sorted_string].append(original_string)
            else:
                freq_map[sorted_string] = [original_string]
        
        for strs_group in freq_map:
            res.append(freq_map[strs_group])
        
        return res


        