class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Create prefix and postfix arrays
        prefix[i] is product of all numbers before nums[i]
        suffix[i] is product of all numbers after nums[i]
        '''
        prefix = self.create_prefix(nums) 
        suffix = self.create_suffix(nums) 
        result = []
        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i])
        
        return result

    def create_prefix(self, nums: List[int]) -> List[int]:
        prefix = []
        for i in range(len(nums)):
            prefix.append(1)
        
        i = 1 # skip first index
        while i < len(nums):
            prefix[i] = prefix[i - 1] * nums[i - 1]
            i += 1
        
        return prefix

    def create_suffix(self, nums: List[int]) -> List[int]:
        suffix = []
        for i in range(len(nums)):
            suffix.append(1)
        
        i = len(nums) - 2 # skip last num
        while i >= 0:
            suffix[i] = suffix[i + 1] * nums[i + 1] 
            i -= 1

        return suffix
