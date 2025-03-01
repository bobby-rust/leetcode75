class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Trivial case
        if len(word1) != len(word2): return False

        word1_freq, word2_freq = Counter(word1), Counter(word2)
        return sorted(word1_freq.values()) == sorted(word2_freq.values()) and set(word1) == set(word2)
