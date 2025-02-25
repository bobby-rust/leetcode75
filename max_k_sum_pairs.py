class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # easy to see a brute force solution for n^2
        # but do we need to check every combination?
        # probably not, if we sort the array first
        # we can just start with 2 pointers
        # and if the current sum is too small,
        # move a pointer up and if its too big, 
        # move a pointer back
        nums.sort()
        l = 0
        r = len(nums) - 1
        result = 0
        while l < r:
            s = nums[l] + nums[r]
            if s == k:
                result += 1
                # stop looking at these two
                # as we just used them so 
                # they cannot be used again
                l += 1
                r -= 1
            elif s < k:
                l += 1
            else:
                r -= 1
                
        return result
