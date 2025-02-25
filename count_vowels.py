class Solution:
    def count_vowels(self, s: str) -> int:
        vowels='aeiou'
        n = 0
        for c in s:
            if c in vowels:
                n += 1
        return n

    def maxVowels(self, s: str, k: int) -> int:
        # literally the same as the previous problem what?
        # only instead of subtracting the sum im subtracting 
        # the num of vowels

        vowels = 'aeiou'
        i = 0
        cv = self.count_vowels(s[:k])
        mv = cv
        while i + k < len(s):
            if s[i] in vowels:
                cv -= 1
            if s[i + k] in vowels:
                cv += 1

            mv = max(mv, cv)
            i += 1
        return mv
