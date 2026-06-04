from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '/' + s 
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            
            while j < len(s) and s[j] != '/':
                j += 1

            # Check for malformed string (delimiter missing at end)
            if j == len(s):
                return res 
                
            length = int(s[i:j])
            
            start_word_index = j + 1
            end_word_index = start_word_index + length
            
            # Check for malformed string (word truncated)
            if end_word_index > len(s):
                 # Handle error case by just stopping
                 return res
            
            word = s[start_word_index : end_word_index]
            res.append(word)
            
            i = end_word_index 
            
        return res