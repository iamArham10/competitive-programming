class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        present_nums = set(nums)
        longest_seq = 0
        for num in nums:
            prev = num - 1
            if prev in present_nums:
                continue
            # start of the sequence
            local_seq_length = 1
            while num+1 in present_nums:
                local_seq_length += 1
                num += 1
            longest_seq = max(longest_seq, local_seq_length)
        
        return longest_seq
            

            


        
        