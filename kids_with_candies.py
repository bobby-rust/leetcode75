class Solution:
    def unsigned_arr_max(self, arr: List[int]):
        max = 0
        for el in arr:
            if el > max:
                max = el
        return max
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Find the max number of candies in the array before giving out any extra candies
        # loop through this array, keeping track of i
        # if candies[i] + extraCandies >= maxCandies -> result[i] = True
        max_candies = self.unsigned_arr_max(candies)
        result = []
        for kid in candies:
            result.append(kid + extraCandies >= max_candies)

        return result
        
