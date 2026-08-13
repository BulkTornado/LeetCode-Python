

class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False

        if x < 0:
            x = -x
            is_negative = True

        x = int(str(x)[::-1])

        if x not in range(-2**31, 2**31-1):
            return 0

        if is_negative:
            x = -x

        return x