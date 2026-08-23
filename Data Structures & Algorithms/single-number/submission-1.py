class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xored = 0

        for num in nums:
            xored = xored ^ num
        return xored