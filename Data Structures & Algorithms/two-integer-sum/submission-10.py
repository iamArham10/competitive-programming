class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i in range(nums):
            if mydict.get(target - nums[i]) is not None:
                return [mydict.get(target - nums[i]), i]
            mydict[nums[i]] = i
