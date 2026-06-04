class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = []
        postfix = [0] * len(nums) 

        for i in range(len(nums)):
            num = nums[i]
            if i != 0:
                num = num * prefix[i-1]
            prefix.append(num)

        for j in range(1,len(nums)+1):
            num = nums[-j]
            if -j != -1:
                num = num * postfix[-j+1]
            postfix[-j] = num
        
        for i in range(len(nums)):
            if i == 0:
                res.append(postfix[1])
            elif i == len(nums)-1:
                res.append(prefix[len(nums)-2])
            else:
                multiplication = prefix[i-1]*postfix[i+1]
                res.append(multiplication)
        
        return res

        