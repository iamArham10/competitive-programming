class Solution:
    def hammingWeight(self, n: int) -> int:

        numberOfBits = 0
        for i in range(32):
            numberOfBits += (n >> i) & 1
        
        return numberOfBits
         
        
        