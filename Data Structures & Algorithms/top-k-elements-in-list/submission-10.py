from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        res = []

        for num, count in freq.items():
            element = (count,num)
            if len(heap) < k:
                heapq.heappush(heap, element)
            else:
                if count > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, element)
        
        for count, num in heap:
            res.append(num)
            
        return res


