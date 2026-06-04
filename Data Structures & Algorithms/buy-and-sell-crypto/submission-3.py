class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #input: prices = [3,2,1,4,5,6,1]
        #                 |   |
        #if left bigger than right move left
        #if same move right
        #if right bigger move right
        max_profit = 0
        left = 0 
        for right in range(len(prices)):
            buy = prices[left]
            sell = prices[right]

            if buy > sell:
                left=right
                
            max_profit = max(max_profit, sell - buy)

        return max_profit



        