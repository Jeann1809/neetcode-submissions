class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #input: height = [1,7,2,5,4,7,3,6]
        #                   |         |
        #
        # w = 6-1 = 5 height = min(l,r) = 3
        #max_area = 36
        max_area = 0
        left = 0
        right = len(heights)-1
        while left < right:
            w = right - left
            h = min(heights[left], heights[right])

            new_area = w * h
            max_area = max(new_area, max_area)
            if heights[left] > heights[right]:
                right-=1
            else:
                left+=1
        return max_area