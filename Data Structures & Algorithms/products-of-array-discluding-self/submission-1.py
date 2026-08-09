class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftArray = [1] * len(nums)
        rightArray = [1] * len(nums)

        for i in range(1, len(nums)):
            leftArray[i] = leftArray[i-1]*nums[i-1]
        for i in range(len(nums)-2, 0, -1):
            rightArray[i] = rightArray[i+1]*nums[i+1]
        
        result = [leftArray[i]*rightArray[i] for i in range(len(nums))]
        return result
        