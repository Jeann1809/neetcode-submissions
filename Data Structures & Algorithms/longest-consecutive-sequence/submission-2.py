class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # input : nums = [2,20,4,10,3,4,5]
        # nums_set = [2,20,4,10,3,4,5]
        # sorted_array = [2,3,4,5,10,20] -> 2,3,4,5 
        max_streak = 0
        streak = 1

        nums_set = set(nums)
        sorted_arr = sorted(nums_set)
        print(sorted_arr)

        if nums == []:
            return 0
        
        for i in range(1,len(sorted_arr)):
            if sorted_arr[i-1] == sorted_arr[i]-1:
                streak +=1
            else:
                max_streak = max(max_streak, streak)
                streak = 1

        max_streak = max(max_streak, streak)

        return max_streak



        