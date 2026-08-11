

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        x: str = str(x)

        length: int = len(str(x))
        l_ptr = 0
        r_ptr = length - 1

        while l_ptr < r_ptr:
            if x[l_ptr] != x[r_ptr]:
                return False
            l_ptr += 1
            r_ptr -= 1

        return True