from functools import reduce

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        is_negative = False

        if x < 0:
            x = -x
            is_negative = True

        rev_num = []

        while x > 0:
            rev_num.append(x % 10)
            x = x // 10

        x = reduce(lambda _x, _y: _x * 10 + _y, rev_num)

        if x not in range(-2**31, 2**31-1):
            return 0

        if is_negative:
            x = -x

        return x