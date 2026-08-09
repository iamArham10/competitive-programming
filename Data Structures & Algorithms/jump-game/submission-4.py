class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp solution
        memo = {}
        def reach(nums, i):
            
            if i == len(nums)-1:
                return True

            if i in memo:
                return memo[i]

            result = False

            for j in range(1, nums[i]+1):
                if (i + j < len(nums)):
                    memo[i+j] = reach(nums, i + j)
                    result = result or memo[i+j]
            
            return result
        
        return reach(nums, 0)




        