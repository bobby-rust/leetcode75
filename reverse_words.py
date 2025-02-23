class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        I'm going to assume that a function to split by spaces doesn't exist

        Once I have a list of the words in the string,
        it's as simple as iterating backwards and building a new string
        '''
        stripped = self.strip(s)
        i = 0
        word = ""
        words = []
        while i < len(stripped):
            if stripped[i] != " ":
                word += stripped[i]
                i += 1
            else:
                words.append(word)
                word = ""
                i = self.advance(stripped, i)

            if i == len(stripped):
                words.append(word)

        result = "" 
        # iterate backwards through words
        for j in range(len(words) - 1, -1, -1):
            if j != 0:
                result += words[j] + " "
            else:
                result += words[j]
        return result 

    def lstrip(self, s: str) -> str:
        '''
        Removes whitespace from the beginning of s
        Return a new string that starts with a character 
        '''
        i = 0
        while s[i] == " ":
            i += 1

        result = ""
        while i < len(s):
            result += s[i]
            i += 1

        return result

    def rstrip(self, s: str) -> str:
        '''
        Removes whitespace from the end of a s
        Returns a new string that ends with a character
        ''' 
        # Find the last character in s
        i = len(s) - 1
        while s[i] == " ":
            i -= 1

        # Build a new string from s[0] to s[i]
        result = "" 
        j = 0
        while j <= i:
            result += s[j]
            j += 1

        return result
    
    def strip(self, s: str) -> str:
        l = self.lstrip(s)
        r = self.rstrip(l)
        return r

    # when we see a space, we know the current word is over and 
    # we want to advance (consume whitespace chars) until the next word 
    def advance(self, s: str, i: int) -> str:
        '''
        Returns the index of the next character in s
        '''
        while s[i] == " " and i < len(s) - 1:
            i += 1

        return i
