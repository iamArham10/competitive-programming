class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        i = 0
        j = 0
        my_set = set()
        global_max = 0
        while (j < len(s)):
            if (s[j] not in my_set):
                my_set.add(s[j])
                j += 1

                global_max = max(global_max, j - i)
            else:
                # at this stage s[j] is in the set
                my_set.discard(s[i])
                i += 1
        return global_max


        
        