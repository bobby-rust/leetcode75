class Solution:
    def extractBrackets(self, s: str) -> str:
        i = 1
        stack = [1]
        contents = ""
        while stack and i < len(s):
            contents += s[i]
            if s[i] == '[':
                stack.append(1)
            elif s[i] == ']':
                stack.pop()
            i += 1
        contents = contents[:-1]
        return contents
        
    def decodeString(self, s: str) -> str:
        # Base case
        if '[' not in s:
            return s
        result = ""
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = ""
                while s[i].isdigit():
                    num += s[i] 
                    i += 1
                # now we are past the digit, should be at a bracket.
                # now we should extract the brackets and call decode string on that
                contents = self.extractBrackets(s[i:])
                result += int(num) * self.decodeString(contents)
                i += len(contents) + 1
            else:
                result += s[i]
            i += 1
                
        return result
