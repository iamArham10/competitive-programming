from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def getKey(word: str)-> tuple[int]:
            myCounter = [0] * 26
            for c in word:
                index = ord(c) - ord('a')
                myCounter[index] += 1
            return tuple(myCounter)
        
        groups = defaultdict(list)

        for word in strs:
            key = getKey(word)
            groups[key].append(word)
        
        result = []
        for (key, value) in groups.items:
            result.append(value)
        
        return result

        

        