from sys import maxsize

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # First, find an increasing double
        # But as we iterate through, keep track of  
        # the smallest increasing double so far
        left, right = maxsize, maxsize
        for n in nums:
            if n <= left:
                left = n
            elif n <= right:
                right = n
            if left < right and right < n:
                return True

        return False
