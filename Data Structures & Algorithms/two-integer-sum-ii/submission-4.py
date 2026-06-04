class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers= [1,2,3,5,7,8,9] target = 7
        #           . .  .  .
        l = 0
        r = len(numbers)-1

        while l < r:
            if numbers[l] + numbers[r] > target: 
                r-=1
            elif numbers[l] + numbers[r] < target:
                l+=1
            else:
                return [l+1,r+1]




        