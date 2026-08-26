class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.getSquareSum(n)

        while fast != 1 and slow != fast:
            slow = self.getSquareSum(slow)
            fast = self.getSquareSum(self.getSquareSum(fast))
        return fast == 1


    def getSquareSum(self, n: int) -> int:
        square_sum = 0
        while n != 0:
            square_sum += (n % 10) ** 2
            n = n // 10
        return square_sum

        
