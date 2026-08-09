class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i in range(len(nums)):
            if mydict.get(nums[i] - target) is not None:
                return [mydict.get(nums[i] - target), i]
            mydict[nums[i]] = i
        return [] 
