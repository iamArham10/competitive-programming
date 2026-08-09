class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        l = 0
        r = 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l,r+1):
                farthest = max(farthest, nums[i] + i)
            steps += 1
            l = r + 1
            r = farthest
        return steps



            

                



         
        