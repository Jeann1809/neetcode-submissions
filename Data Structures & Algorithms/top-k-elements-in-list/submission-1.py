class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        res = []

        for i in range(k):
            max_val = 0
            max_count = 0
            print(freq_map)
            for num in freq_map:
                if freq_map[num] > max_count:
                    max_count = freq_map[num]
                    max_val = num
            freq_map[max_val] = 0
            res.append(max_val)
        
        return res

                

        