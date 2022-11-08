class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        #variables for arithmetic
        carry = 0
        mult = 1
        #convert strings to lists
        num1, num2 = list(num1), list(num2)
        #loop until lists are empty
        while num1 or num2 or carry:
            s = carry
            # pop digits from back one by one to prevent offset
            if num1:
                s += int(num1.pop())
            if num2:
                s += int(num2.pop())
                
            if s >= 10:
                s -= 10
                carry = 1
            else:
                carry = 0
            
            res += str(s)
            
        return res[::-1]
        
        