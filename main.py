from pathlib import Path

ROOT = Path(__file__).parent
PROBLEMS = ROOT / "problems"
SOLUTIONS = ROOT / "src" / "solutions"
LEETCODE_TYPES = ROOT / "src" / "leetcode_types"
TESTS = ROOT / "tests"

sub_one_for_init = 1

def count_files(directory: Path, pattern: str) -> int:
    return len(list(directory.glob(pattern)))

def main():
    problems = count_files(PROBLEMS, "*.md")
    solutions = count_files(SOLUTIONS, "_*.py") - sub_one_for_init
    leetcode_types = count_files(LEETCODE_TYPES, "*.py") - sub_one_for_init
    tests = count_files(TESTS, "test_*.py")

    print()
    print("LeetCode Solutions in Python")
    print()
    print(f"Problems       : ./problems           : {problems}")
    print(f"Solutions      : ./src/solutions      : {solutions}")
    print(f"LeetCode Types : ./src/leetcode_types : {leetcode_types}")
    print(f"Tests          : ./tests              : {tests}")
    print()
    print("Run all tests:")
    print("    uv run pytest")
    print()
    print("Run a specific test:")
    print("    uv run pytest tests/test_0001_Two_Sum.py")
    print()
    print("Run a specific unit test:")
    print("    uv run pytest tests/test_0001_Two_Sum.py::test_two_sum_1")

if __name__ == '__main__':
    main()
