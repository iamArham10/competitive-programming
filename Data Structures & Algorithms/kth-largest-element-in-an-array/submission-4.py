class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def partition(i, j):
            pivot = nums[(i + j) // 2]
            left = i
            right = j

            while left <= right:
                while nums[left] > pivot:
                    left += 1

                while nums[right] < pivot:
                    right -= 1

                if left <= right:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1

            return left

        target = k - 1
        left = 0
        right = len(nums) - 1

        while left < right:
            index = partition(left, right)

            if target < index:
                right = index - 1
            else:
                left = index

        return nums[left]