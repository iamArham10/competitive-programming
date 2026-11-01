class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        output = []
        candidates.sort()

        def dfs(target, result, i):
            if target < 0:
                return
            if target == 0:
                output.append(result.copy())
                return
            if i >= len(candidates):
                return


            result.append(candidates[i])
            dfs(target-candidates[i], result, i+1)
            result.pop()
            j = i+1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            dfs(target, result, j)
        
        dfs(target, [], 0)

        return output