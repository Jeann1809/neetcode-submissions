class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        nums_len = len(nums)
        bucket_list = [[] for _ in range(nums_len+1)]
        res = []

        for num in nums:
            freq_map[num] = freq_map.get(num,0)+1
        
        for number , count in freq_map.items():
            bucket_list[count].append(number)
        
        for i in range(nums_len, 0, -1):
            for freq_element in bucket_list[i]:
                if k > 0:
                    res.append(freq_element)
                    k-=1
        return res


