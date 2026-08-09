class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i, num in enumerate(nums):
            reqIndices = mydict.get(target-num)
            if reqIndices:
                return [reqIndices, i]
            mydict[i] = num
