class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # keep track of current position of s
        # loop through t and if we find s[i], increment i
        # if i == len(t) - 1, true else false
        
        # trivial case, ε is a subsequence of ε
        if s == "" and t == "":
            return True
            
        i = 0
        for c in t:
            if i < len(s) and s[i] == c:
                i += 1
            if i == len(s):
                return True
    
        return False
        
