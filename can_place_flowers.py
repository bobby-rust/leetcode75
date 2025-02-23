class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # keep track of current - 1 and current + 1
        # if current - 1 and current + 1 are both 0, n--
        # at the end, if n <= 0, return True
        # else return False
        # Edge case includes first and last element
        # For first element, plant if second element is empty, else don't plant
        # For last element, plant if second-to-last element is empty, else don't plant
        # Also need to keep track of the changes I'm making to flowerbed

        if len(flowerbed) == 1:
            return (n == 1 and flowerbed[0] == 0) or n == 0 

        flowers_to_plant = n
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
                
            # First flowerpot is an edge case
            if i == 0:
                if flowerbed[1] == 0:
                    flowerbed[0] = 1
                    flowers_to_plant -= 1
                    continue
            # Last flowerpot is an edge case
            if i == len(flowerbed) - 1:
                if flowerbed[-2] == 0:
                    flowerbed[-1] = 1
                    flowers_to_plant -= 1
                    break

            if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                flowers_to_plant -= 1

            # No need to keep checking
            if flowers_to_plant <= 0:
                return True

        # No need to keep checking
        if flowers_to_plant <= 0:
            return True
        return False
