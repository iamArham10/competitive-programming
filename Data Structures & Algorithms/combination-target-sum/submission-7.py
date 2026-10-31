class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        def dfs(result, cur, i):
            if (cur == 0):
                output.append(result.copy())
                return
            if (cur < 0):
                return

            for n in range(i, len(nums)):
                num = nums[n]
                result.append(num)
                dfs(result, cur-num, n)
                result.pop()

        dfs([], target, 0)
        return output
    
        