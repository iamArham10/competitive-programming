class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        while (l < r):
            if not str.isalnum(s[l]):
                l += 1
            if not str.isalnum(s[r]):
                r -= 1

            if s[l] != s[i]:
                return False 
            
        return True 

        