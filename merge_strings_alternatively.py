class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = 0
        result = ""
        while (n < len(word1) and n < len(word2)):
            result += word1[n]
            result += word2[n]
            n += 1
        if n < len(word1):
            result += word1[n:]
        if n < len(word2):
            result += word2[n:]
        return result
