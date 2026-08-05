from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCounter = Counter(nums)

        frequency = [[] for _ in range(len(nums) + 1)]
        for value, freq in numCounter.items():
            frequency[freq].append(value)

        # get the numbers
        result = []
        for i in range(len(nums), 0, -1):
            for num in frequency[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result
