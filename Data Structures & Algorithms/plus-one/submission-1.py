class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]

        toAddOne = True
        for i in range(len(digits)):
            if toAddOne:
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    toAddOne=False
        
        if toAddOne:
            digits.append(1)
        return digits[::-1]
                
            


            