#input: nums = [1,2,3,4,5]
#output: 5

#input: nums = [3,5,7,1,4]
#output: 3

'''
PLAN:
1. Create a hashmap for every number, the key is the number itself and the value is the consecutive number
2. 

'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_count = 0
        for n in nums:
            if n - 1 not in nums_set:
                count = 1
                while n + 1 in nums_set:
                    count += 1
                    n += 1
                if count > max_count:
                    max_count = count
        return max_count
            

        
        