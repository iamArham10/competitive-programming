class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -1
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if (curr_sum < 0):
                curr_sum = 0
            else:
                max_sum = max(max_sum, curr_sum)

        return max_sum

            
        