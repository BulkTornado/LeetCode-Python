from src import Solution_0001_Two_Sum

def main():
    test = Solution_0001_Two_Sum()

    # Test 1
    nums01 = [2, 7, 11, 15]
    result01 = test.twoSum(nums01, 9)
    print(result01)

    # Test 2
    nums02 = [3, 2, 4]
    result02 = test.twoSum(nums02, 6)
    print(result02)

    # Test 3
    nums03 = [3, 3]
    result03 = test.twoSum(nums03, 6)
    print(result03)

if __name__ == '__main__':
    main()