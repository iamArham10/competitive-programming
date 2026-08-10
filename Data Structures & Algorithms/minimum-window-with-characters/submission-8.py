class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        
        t_count = {}
        window = {}

        for c in t:
            t_count[c] = t_count.get(c, 0) + 1
        
        matched, required = 0, len(t_count)
        result, min_result_length = [], float("infinity") 

        l = 0
        for r in range(len(s)):
            c = s[r]
            
            # if right char from s is in the t string, we need to update count
            if c in t_count:
                window[c] = window.get(c, 0) + 1
                if t_count[c] == window[c]:
                    matched += 1
            
            # if we have found a contender for a substring
            while matched == required:
                if (r - l + 1) < min_result_length:
                    result = [l, r]
                    min_result_length = r - l + 1
                
                # lets try to minimize it
                if s[l] in t_count:
                    window[s[l]] -= 1
                    if window[s[l]] < t_count[s[l]]:
                        matched -= 1 
                l += 1

        if min_result_length == float("infinity"): return ""
        l, r = result

        return s[l:r+1]

        




            


