from solutions import Solution_0002_Add_Two_Numbers
from leetcode_types import ListNode

solution = Solution_0002_Add_Two_Numbers()

def test_add_two_numbers_1():
    l1: ListNode = ListNode.list_to_linked_list([2,4,3])
    l2: ListNode = ListNode.list_to_linked_list([5,6,4])

    result = solution.addTwoNumbers(l1, l2)

    assert ListNode.linked_list_to_list(result) == [7,0,8]

def test_add_two_numbers_2():
    l1: ListNode = ListNode.list_to_linked_list([0])
    l2: ListNode = ListNode.list_to_linked_list([0])

    result = solution.addTwoNumbers(l1, l2)

    assert ListNode.linked_list_to_list(result) == [0]

def test_add_two_numbers_3():
    l1: ListNode = ListNode.list_to_linked_list([9,9,9,9,9,9,9])
    l2: ListNode = ListNode.list_to_linked_list([9,9,9,9])

    result = solution.addTwoNumbers(l1, l2)

    assert ListNode.linked_list_to_list(result) == [8,9,9,9,0,0,0,1]