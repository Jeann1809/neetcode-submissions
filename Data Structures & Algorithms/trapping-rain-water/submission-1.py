class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft = [0]
        mleft = 0
        for i in range(1,len(height)):
            mleft = max(mleft, height[i-1])
            maxleft.append(mleft)
        
        maxright = [0]
        mright = 0
        for i in range(len(height)-2,-1,-1):
            mright = max(mright, height[i+1])
            maxright.append(mright)
        maxright = maxright[::-1]

        area = 0
        for i in range(len(height)):
            ml = maxleft[i]
            mr = maxright[i]
            result = min(ml,mr)-height[i]
            if result > 0:    
                area += min(ml,mr) - height[i]
        
        return area
        