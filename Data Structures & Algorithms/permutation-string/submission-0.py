class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # input: s1 = "abc",           s2 = "lecaee"
        #                                       |
        #                                         |
        #freq_s1 = {a: 1, b:2, c:3}
        #freq_s2w = {l:1, ...}

        freq_s1 = {}
        for char in s1:
            freq_s1[char] = freq_s1.get(char, 0) + 1

        left = 0
        right = len(s1)


        while right <= len(s2):
            subs_string = s2[left:right]
            freq_s2 = {}

            for char in subs_string:
                freq_s2[char] = freq_s2.get(char, 0) + 1

            if freq_s1 == freq_s2:
                return True
                
            left +=1
            right +=1

        return False
