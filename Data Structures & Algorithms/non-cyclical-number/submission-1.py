class Solution:
    def isHappy(self, n: int) -> bool:
        hashmap = set()

        while n not in hashmap:
            if n == 1:
                return True
            hashmap.add(n)
            n = self.getSquareSum(n)
        return False


    def getSquareSum(self, n: int) -> int:
        square_sum = 0
        while n != 0:
            square_sum += (n % 10) ** 2
            n = n // 10
        return square_sum

        
