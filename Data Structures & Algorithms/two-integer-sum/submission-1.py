class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_len = len(nums)
        hash_map = {}
        for i in range(nums_len):
            complement = target - nums[i]
            if complement in hash_map:
                index = hash_map[complement]
                return [index,i]
            else:
                hash_map[nums[i]] = i
        return 0
