# Problem no - Add Binary

# Time complexity O(max(m, n) where m and n are lengths of input a and b

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1 = int(a, 2)
        num2 = int(b, 2)
        if num1 + num2 == 0:
            return "0"
        div_result = 0
        output = ""
        while num1 or num2:
            summa = (num1 & 1) + (num2 & 1) + div_result
            div_result = summa // 2
            output += str(summa % 2)
            num1 = num1 >> 1
            num2 = num2 >> 1
        if div_result:
            output += str(div_result)
        return output[::-1]
