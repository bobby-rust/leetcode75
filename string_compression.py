class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        while i < len(chars):
            n = 1
            while i < len(chars) - 1 and chars[i] == chars[i + 1]:
                n += 1
                i += 1

            ncpy = n 
            while n > 1:
                del chars[i]
                i -= 1
                n -= 1 
            if ncpy > 1:
                for c in str(ncpy):
                    chars.insert(i + 1, c)
                    i += 1
                

            i += 1
        return len(chars)
