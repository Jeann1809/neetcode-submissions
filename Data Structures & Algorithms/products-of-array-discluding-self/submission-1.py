class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #input: nums = [1,2,3,4]            =>           out = [24,12,8,6]
        #       prefix = [1,1,2,6] 
        #       postfix = [24,12,4,1]

        nums_len = len(nums)
        output = []
        #initialize prefix and postfix
        prefix = [1] * nums_len
        postfix = [1] * nums_len

        #prefix logic
        for i in range(1,nums_len):
            prefix[i] = nums[i-1]*prefix[i-1]
        
        #postfix logic
        for i in range(nums_len-2,-1,-1):
            postfix[i] = nums[i+1]*postfix[i+1]

        for i in range(nums_len):
            multiplication = prefix[i] * postfix[i]
            output.append(multiplication)
        
        return output
            


