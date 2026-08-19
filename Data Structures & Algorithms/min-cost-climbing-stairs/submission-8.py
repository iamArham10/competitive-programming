class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        secondLast, last = cost[0], cost[1]
        for i in range(2, len(cost)):
            cost_at_i = cost[i] + min(secondLast, last)
            secondLast = last
            last = cost_at_i
        
        return min(last, secondLast)
        