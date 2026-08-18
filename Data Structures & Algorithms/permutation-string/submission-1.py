class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorted1 = sorted(s1)

        l,r = 0,len(s1)-1

        while r < len(s2):
            temp = sorted(s2[l:r+1])

            if temp == sorted1:
                return True
            else:
                l+=1
                r+=1
        return False



        