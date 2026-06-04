from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        res = []

        for num in freq:
            element = (freq[num],num)
            if len(heap) < k:
                heapq.heappush(heap, element)
            elif freq[num] > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, element)
        
        for index, num in heap:
            res.append(num)

        return res

