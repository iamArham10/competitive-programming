class Solution:
    def hammingWeight(self, n: int) -> int:

        numberOfBits = 0
        while (n):
            n = n & (n-1)
            numberOfBits +=1
        return numberOfBits
         
        
        