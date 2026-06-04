import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # input: piles = [1,2,3,4]  , h = 6, output = 2
        # k = [1,2,3,4]
        max_k = max(piles)
        res = max(piles)

        left, right = 1 , max_k

        while left <= right:
            k = (right + left) // 2
            count = 0
            for pile in piles:
                count += math.ceil(pile/k)

            if count <= h:
                right = k - 1
                res = min(k, res)
            else:
                left = k + 1

        return res

        
        