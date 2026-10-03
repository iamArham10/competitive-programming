class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_bananas = float("-inf")
        for p in piles:
            max_bananas = max(max_bananas, p)

        lo = 1
        hi = max_bananas
        result = hi

        def simulate(piles, k, h):

            time = 0
            for p in piles:
                time += math.ceil(p/k)
            
            return time <= h

        while lo <= hi:
            mid = lo + (hi - lo)//2

            if simulate(piles, mid, h):
                result = min(result, mid)
                hi = mid - 1
            else:
                lo = mid + 1

        return result
            





        
        