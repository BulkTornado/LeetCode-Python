

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        div = 10**(len(str(x)) - 1)

        while x:
            left = x // div
            right = x % 10

            if left != right:
                return False
            x = (x % div) // 10
            div /= 100

        return True