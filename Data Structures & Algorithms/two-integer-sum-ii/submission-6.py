class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        Input: numbers = [1,2,3,4], target = 3
        1 + 4
        if move left -> increase the sum
        if move right -> decrease the sum
        so I want to have left and right 
        and whenever the addition is higher to target I move my right to left
        and when lower than target i move left pointer
        If left greater that right I return false
        Output: [1,2]
        '''
        l = 0
        r = len(numbers)-1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1,r+1]
            
            if numbers[l] + numbers[r] < target:
                l+=1
            else:
                r-=1

        return []
        