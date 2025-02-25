from typing import List
from sys import maxsize

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # okay so .... just iterate through the list once with a 
        # k-sized window... need to check all possible anyways..
        # getting TLE, so my first thought is i don't have to recompute
        # the full sum every iteration. huge waste.
        # just take the sum initially and 
        # when incrementing, subtract the first value
        # in the window, and next iteration add only the last
        # value to the running sum
        
        i = 0
        max_sum = -maxsize - 1
        cur_sum = sum(nums[0:k])
        while i < len(nums) - k + 1:
            max_sum = max(max_sum, cur_sum)
            cur_sum -= nums[i]
            if i + k < len(nums):
                cur_sum += nums[i + k]
            else:
                break
            i += 1 

        return max_sum / k
