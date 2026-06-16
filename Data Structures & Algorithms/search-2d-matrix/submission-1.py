class Solution:
    def binary(self, arr,  left, right, target):
        if right<left and arr[0] != target:
            return False

        
        mid = int((right+left)/2)

        if arr[mid] > target:
            return self.binary(arr,left,mid-1,target)
        elif arr[mid] < target:
            return self.binary(arr,mid+1,right,target)
        else:
            return True
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target in range(matrix[i][0],matrix[i][-1]+1):
                return self.binary(matrix[i],0,len(matrix[i])-1,target)
        return False

        