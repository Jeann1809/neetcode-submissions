import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for num in nums:
            freq_map[num] = freq_map.get(num,0)+1
        
        heap = []
        for num,freq in freq_map.items():
            heapq.heappush(heap,(freq,num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for freq , num in heap:
            res.append(num)
        
        return res



        