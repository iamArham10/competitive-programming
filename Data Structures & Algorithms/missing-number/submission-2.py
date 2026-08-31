class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = 0
        for i in range(len(nums)+1):
            n ^= i
        for i in nums:
            n ^= i
        return n
        