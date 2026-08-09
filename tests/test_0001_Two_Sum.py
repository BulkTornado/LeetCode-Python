from solutions import Solution_0001_Two_Sum

solution = Solution_0001_Two_Sum()

def test_two_sum_1():
    nums_1 = [2, 7, 11, 15]
    result_1 = solution.twoSum(nums_1, 9)
    assert sorted(result_1) == [0, 1]

def test_two_sum_2():
    nums_2 = [3, 2, 4]
    result_2 = solution.twoSum(nums_2, 6)
    assert sorted(result_2) == [1, 2]

def test_two_sum_3():
    nums_3 = [3, 3]
    result_3 = solution.twoSum(nums_3, 6)
    assert sorted(result_3) == [0, 1]