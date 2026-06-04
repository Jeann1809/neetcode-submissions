class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        1. Sort the array
        2. Iterate though the array to find first position A, and make sure we dont repeat that value
        3. Two pointers left and right to find the other the difference
        4. Add those numbers to the result arrat
        5. Return the result array
        '''

        res = []
        nums_sorted = sorted(nums)
        n = len(nums)
        prev = None
        for start in range(n-2):
            if nums_sorted[start] == prev:
                continue

            prev = nums_sorted[start]

            left = start+1
            right = n-1

            while left < right:
                a = nums_sorted[start]
                b = nums_sorted[left]
                c = nums_sorted[right]

                if a + b + c == 0:
                    if [a,b,c] not in res:
                        res.append([a,b,c])
                    left += 1
                    right -=1
                
                if a + b + c > 0:  #If i want a smaller result, move right pointer
                    right -= 1
                if a + b + c < 0:
                    left += 1

        return res
        