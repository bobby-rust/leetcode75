class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r, largest, flipped = 0, 0, 0, 0
        while r < len(nums):
            if nums[r] == 0:
                flipped += 1
            while flipped > k:
                if nums[l] == 0:
                    flipped -= 1
                l += 1
            largest = max(largest, r - l + 1)
            r += 1
        return largest
