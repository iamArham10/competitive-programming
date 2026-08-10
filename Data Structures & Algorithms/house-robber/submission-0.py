class Solution:
    def rob(self, nums: List[int]) -> int:
        beforeHouse, beforeBeforeHouse = 0, 0
        for num in nums:
            newRob = max(beforeBeforeHouse + num, beforeHouse)
            beforeBeforeHouse = beforeHouse
            beforeHouse = newRob
        
        return beforeHouse
        