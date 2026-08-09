class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        while (l < r):
            while not str.isalnum(s[l]):
                l += 1
                continue
            while not str.isalnum(s[r]):
                r -= 1
                continue

            if s[l] != s[r]:
                return False 

            l += 1
            r -= 1
            
        return True 

        