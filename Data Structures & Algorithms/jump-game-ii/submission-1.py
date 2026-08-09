class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float("+inf")] * len(nums)
        dp[0] = 0

        for i in range(nums):
            for j in range(1, nums[i]+1):
                nums[i+j] = min(dp[i+j], 1 + dp[i])
        
        return nums[len(nums)-1]
                



         
        