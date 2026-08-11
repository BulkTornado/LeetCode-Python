from solutions import Solution_0009_Palindrome_Number

solution = Solution_0009_Palindrome_Number()

def test_palindrome_number_1():
    x: int = 121
    output: bool = solution.isPalindrome(x)

    assert output == True

def test_palindrome_number_2():
    x: int = -121
    output: bool = solution.isPalindrome(x)

    assert output == False

def test_palindrome_number_3():
    x: int = 10
    output: bool = solution.isPalindrome(x)

    assert output == False