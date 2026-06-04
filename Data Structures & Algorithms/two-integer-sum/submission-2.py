class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # input: [1,2,3,4,5] target = 8
        #             .   .
        # values = {1:0, 2:1, 3:2, 4:3}
        values = {}
        nums_len = len(nums)
        for i in range(nums_len):
            difference = target - nums[i]
            if difference in values:
                j = values[difference]
                return [j,i]
            values[nums[i]] = i
        return 
        