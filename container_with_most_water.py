class Solution:
    def maxArea(self, height: List[int]) -> int:
        # start at largest width
        # decrement right pointer if 
        # height[right] < height[left]
        # if height[left] < height[right]
        # increment left ptr

        max_area = 0
        r = len(height) - 1
        l = 0
        while l < r:
            cur_area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, cur_area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
