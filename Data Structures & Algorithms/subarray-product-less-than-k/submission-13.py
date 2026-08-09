class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        result = 0
        l = 0
        r = 0
        running_product = 1
        while r < len(nums):
            running_product *= nums[r]

            while running_product >= k:
                running_product //= nums[l]
                l += 1
            result += r - l + 1
            r += 1
        return result
            


        