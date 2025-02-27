class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # assume there is not a built in function 
        # that accomplishes the difference between sets
        # because that would be too boring
        s1 = set(nums1)
        s2 = set(nums2)

        l1 = []

        for n in s1:
            if n not in s2:
                l1.append(n)
        l2 = []
        for n in s2:
            if n not in s1:
                l2.append(n)
        return [l1, l2]
