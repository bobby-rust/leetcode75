class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Build a hashmap and test if creating a set from the values
        # of the hashmap is the same length as the array of the values
        occurrences = {}

        for n in arr:
            if n not in occurrences:
                occurrences[n] = 1
            else:
                occurrences[n] += 1

        return len(occurrences.values()) == len(set(occurrences.values()))
