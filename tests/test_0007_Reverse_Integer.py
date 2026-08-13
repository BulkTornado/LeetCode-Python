from solutions import Solution_0007_Reverse_Integer

solution = Solution_0007_Reverse_Integer()

def test_reverse_integer_1():
    x = 123
    expected_result = 321
    result = solution.reverse(x)

    assert result == expected_result

def test_reverse_integer_2():
    x = -123
    expected_result = -321
    result = solution.reverse(x)

    assert result == expected_result

def test_reverse_integer_3():
    x = 120
    expected_result = 21
    result = solution.reverse(x)

    assert result == expected_result

def test_reverse_integer_4():
    x = 1534236469
    expected_result = 0 # 9646324351
    result = solution.reverse(x)

    assert result == expected_result

def test_reverse_integer_5():
    x = 0
    expected_result = 0
    result = solution.reverse(x)

    assert result == expected_result

def test_reverse_integer_6():
    x = 1563847412
    expected_result = 0
    result = solution.reverse(x)

    assert result == expected_result