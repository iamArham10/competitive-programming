class Solution:
    def jump(self, nums: List[int]) -> int:
        nums[i] = [float("+inf")]
        nums[0] = 0

        for i in range(nums):
            for j in range(1, nums[i]+1):
                nums[i+j] = min(nums[i+j], 1 + nums[i])
        
        return nums[len(nums)-1]
                



         
        