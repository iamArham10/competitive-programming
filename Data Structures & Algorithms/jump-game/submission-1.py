class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def reach(nums, i):
            if i == len(nums)-1:
                return True
            result = False
            for j in range(1, nums[i]+1):
                if (i + j < len(nums)):
                    result = result or reach(nums, i + j)
            
            return result
        
        return reach(nums, 0)




        