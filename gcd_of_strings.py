class Solution:
    def isDivisibleBy(self, str1: str, str2: str) -> bool:
        '''
        Returns true if str1 is divisible by str2
        '''
        # Trivial cases
        if len(str2) > len(str1):
            return False
        if str1 == str2:
            return True

        product = str2 
        while len(product) < len(str1):
            product += str2 
            if str1 == product:
                return True

        return False

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Attempt to concatenate the string some number of times to achieve both str2 and str1
        # start with the smaller of the two strings as that is the maximum possible answer
        # then decrease until something is found. If none found, return empty string
        if str1 == str2:
            return str1

        if str1 == "" or str2 == "":
            return "" 

        # WLOG, Ensure str1 is not smaller than str2
        if len(str1) < len(str2):
            tmp = str1
            str1 = str2
            str2 = tmp

        divisor = str2
        while len(divisor) > 0:
            if self.isDivisibleBy(str1, divisor) and self.isDivisibleBy(str2, divisor):
                return divisor
            divisor = divisor[:-1]

        return ""

        
        


        


        





        
        
