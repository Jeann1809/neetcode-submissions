class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Plan:
        Create a hash-map that will contain the num and the index of the number
        Iterate through the array checking if the difference between num and target is in the hasmap
        If it is, return the index of both numbers in hashmap
        If not, add the number and index to the hashmap
        If after iterating the whole array there is no match, return false
        '''

        hash_map = {}
        for i in range(len(nums)):
            if target - nums[i] in hash_map:
                index1 = hash_map[target-nums[i]]
                return [index1,i]

            else:
                hash_map[nums[i]] = i
        return False 





        