class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numb = {}
        for i, num in enumerate(nums):
            reqIndices = numb.get(target-nums)
            if reqIndices:
                return [reqIndices, i]
            numb[i] = num
