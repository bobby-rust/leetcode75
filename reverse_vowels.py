class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        start = 0
        end = len(s) - 1
        s = list(s)
        while (start < end):
            while s[start] not in vowels and start < end:
                start+=1
            while s[end] not in vowels and start < end:
                end -= 1

            # swap s[start] and s[end]
            s[start], s[end] = s[end], s[start]

        return s.join("")
