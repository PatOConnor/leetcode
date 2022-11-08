class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        a, b = list(a), list(b)
        while a or b or carry:
            s = carry
            if a: s += int(a.pop())
            if b: s += int(b.pop())
            
            if s >= 2:
                carry = 1
                s -= 2
            else: 
                carry = 0
                
            res += str(s)
        return res[::-1]
        