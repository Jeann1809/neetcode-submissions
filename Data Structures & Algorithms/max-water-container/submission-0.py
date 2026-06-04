class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        max_val = 0

        while l < r:
            multiplication= min(heights[l],heights[r])*(r-l)
            if multiplication > max_val:
                max_val = multiplication

            if heights[l] >= heights[r]:
                r-=1
            else:
                l+=1
        return max_val