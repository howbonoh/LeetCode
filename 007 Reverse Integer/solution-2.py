class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0: neg = True
        x = abs(x)
        answer = 0
        while x != 0:
            pop = x % 10
            x = int(x / 10)
            answer = answer*10 + pop
        if answer > 2**31 or answer < -2**31:
            return 0
        elif neg == True:
            return -answer
        else:
            return answer