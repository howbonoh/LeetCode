class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg = True
        str_num = list(str(abs(x)))
        start = 0
        end = len(str_num) - 1
        while start < end:
            temp = str_num[start]
            str_num[start] = str_num[end]
            str_num[end] = temp
            start = start + 1
            end = end - 1
        answer = int(''.join(str_num))
        if answer > 2**31 or answer < -2**31:
            return 0
        elif neg == True:
            return (-answer)
        else:
            return answer