class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        
        second_last = 1
        last =  1
        for i in range(n-1):
            last, second_last = second_last + last, last
        
        return last

        
        
        
        