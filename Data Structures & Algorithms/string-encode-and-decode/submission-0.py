class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "$" + word
        return encoded


    def decode(self, s: str) -> List[str]:
        result = []
        for i in range(len(s)):
            count = ""
            while (s[i] != "$"):
                count += s[i]
                i += 1
            count = int(count)
            
            result.append(s[i+1: i+1+count])



