from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCounter = Counter(nums)
        frequency = [[]] * (len(nums) + 1) 

        for value, freq in numCounter.items():
            frequency[freq].append(value)

        # get the numbers
        result = []
        while k > 0:
            for i in range(len(nums) + 1, 0, -1):
                number_appeared_i_times = frequency[i]
                if (len(number_appeared_i_items) > 0):
                    # add them to the results
                    for num in number_appeared_i_items:
                        result.append(num)
                    k -= 1
                    if k == 0:
                        break
        
        return result


         

        


         

        