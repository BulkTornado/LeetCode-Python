from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        values = []
        cur = self

        while cur is not None:
            values.append(str(cur.val))
            cur = cur.next

        return " -> ".join(values)

    def __repr__(self):
        return f"ListNode({str(self)})"

    def __len__(self):
        length = 0
        cur = self

        while cur is not None:
            length += 1
            cur = cur.next

        return length

    @staticmethod
    def linked_list_to_list(node: ListNode) -> List[int]:
        values: List[int] = []

        while node is not None:
            values.append(node.val)
            node = node.next

        return values

    @staticmethod
    def list_to_linked_list(values: list[int]) -> ListNode:
        dummy: ListNode = ListNode()
        cur:   ListNode = dummy

        for value in values:
            cur.next = ListNode(value)
            cur = cur.next

        return dummy.next