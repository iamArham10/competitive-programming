class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        i = 0
        j = 0
        my_set = set()
        local_max = 0
        global_max = 0
        while (j < len(s)):
            if (s[j] not in my_set):
                local_max += 1
                j += 1
            else:
                global_max = max(global_max, local_max)
                local_max = 0
                # at this stage s[j] is in the set
                while (s[i] != s[j]):
                    my_set.discard(s[i])
                    i += 1
        return global_max


        
        