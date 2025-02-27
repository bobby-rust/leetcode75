class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumleft = []
        cursum = 0
        for n in nums:
            cursum += n
            sumleft.append(cursum)

        sumright = []
        cursum = 0
        i = len(nums) - 1
        while i >= 0:
            cursum += nums[i]
            sumright.append(cursum)
            i -= 1
        sumright.reverse()

        print("Sum left: ", sumleft)
        print("Sum right: ", sumright)
        i = 0
        while i < len(nums):
            if sumleft[i] == sumright[i]:
                return i
            i += 1
        return -1
