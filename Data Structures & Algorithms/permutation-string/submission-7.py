class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Counter = [0] * 26 
        s2Counter = [0] * 26
        matches = 0

        for i in range(len(s1)):
            s1Counter[ord(s1[i]) - ord('a')] += 1
            s2Counter[ord(s2[i]) - ord('a')] += 1

        for i in range(26):
            if s1Counter[i] == s2Counter[i]:
                matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            # check for newly r match
            indexRight = ord(s2[r]) - ord('a')
            s2Counter[indexRight] += 1

            # if new char matches
            if s1Counter[indexRight] == s2Counter[indexRight]:
                matches += 1
            # if it used to match before
            elif s1Counter[indexRight] == s2Counter[indexRight] - 1:
                matches -= 1

            # removing from the end
            indexLeft = ord(s2[l]) - ord('a')
            s2Counter[indexLeft] -= 1

            # if removing prev char matches
            if s1Counter[indexLeft] == s2Counter[indexLeft]:
                matches += 1
            # if it used to match before
            elif s1Counter[indexLeft] == s2Counter[indexLeft] + 1:
                matches -= 1
            l += 1

        return matches == 26

            

