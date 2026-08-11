

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        num_list_rev = []

        while x:
            digit = x % 10
            num_list_rev.append(digit)

            x = x // 10

        return num_list_rev == num_list_rev[::-1]