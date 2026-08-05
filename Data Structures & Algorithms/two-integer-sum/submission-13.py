class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i, value in enumerate(nums):
            dif = target - value
            if dif in mydict:
                return [mydict[dif], i]
            mydict[value] = i
        return 