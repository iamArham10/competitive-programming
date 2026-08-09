class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)

        i = 0
        j = 0
        result = 0
        max_freq_element = 0
        while j < len(s):
            counter[s[j]] += 1
            max_freq_element = max(max_freq_element, counter[s[j]])
            subseq_length = j-i+1
            if (subseq_length - max_freq_element <= k):
                result = max(result, subseq_length)
            else:
                i += 1
            j += 1

        return result

                                                                                                                   






        