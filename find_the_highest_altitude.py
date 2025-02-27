class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur_alt = 0
        max_alt = 0
        for n in gain:
            cur_alt += n
            max_alt = max(max_alt, cur_alt)
        
        return max_alt
