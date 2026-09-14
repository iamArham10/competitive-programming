class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        single = nums[0]
        double = nums[0]

        while True:
            single = nums[single]
            double = nums[nums[double]]

            if single == double:
                break

        head = nums[0]
        while head != single:
            head = nums[head]
            single = nums[single]
        
        return head