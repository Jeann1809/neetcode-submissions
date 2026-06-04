class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Frequency map logic
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        #Bucket Sort Logic
        bucket_arr = [[] for i in range(len(nums)+1)]
        for num in freq_map:
            #Index is gonna be the count
            index = freq_map[num]
            print(bucket_arr)
            bucket_arr[index].append(num)

        print(bucket_arr)
        #Creating the result array
        res = []
        i=-1
        while k:
            if bucket_arr[i]:
                for n in bucket_arr[i]:
                    if k != 0:
                        res.append(n)
                        k-=1
            i-=1

        
        
        return res

                

        