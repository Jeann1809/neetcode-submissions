class Solution:
    def binary(self,arr, left,right,min_val):
        '''
        1. check if left > right:
        return min

        2. Get mid point

        3. Check if mid point is less than current min_val

        4. Check if mid point is greater or equal to left, if yes search right
           else search left
        '''

        if left > right:
            return min_val
        
        mid = (right + left) // 2

        if arr[mid] < min_val:
            min_val = arr[mid]

        if arr[mid]>=arr[left]:
            if arr[left] < min_val:
                min_val=arr[left]
            return self.binary(arr, mid+1, right, min_val)
        else:
            return self.binary(arr,left,mid-1,min_val)
        
    def findMin(self, nums: List[int]) -> int:
        return self.binary(nums,0,len(nums)-1,nums[0])
        