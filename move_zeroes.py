class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        numZeroes = 0
        while i < len(nums):
            if nums[i] == 0:
                del nums[i]
                numZeroes += 1
                i -= 1
            i += 1

        while numZeroes > 0:
            nums.append(0)
            numZeroes -= 1
            
