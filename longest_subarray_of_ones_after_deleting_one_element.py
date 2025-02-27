class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Find a buncha ones
        # Then find a 0
        # then finda buncha more ones
        # idk man

        l, r, m, flipped = 0, 0, 0, 0
        while r < len(nums):
            if nums[r] == 0:
                flipped += 1
            while flipped > 1:
                if nums[l] == 0:
                    flipped -= 1
                l += 1
            m = max(m, r - l)
            r += 1
        return m
