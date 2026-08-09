class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i in range(nums):
            if target - nums[i] in mydict:
                return [mydict.get(target - nums[i]), i]
            mydict[nums[i]] = i
        return None
