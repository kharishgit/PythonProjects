# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Create a dummy node to simplify merging
        dummy = ListNode(0)
        # Current pointer to build the merged list
        current = dummy

        # While both lists have nodes
        while list1 and list2:
            # Compare values and pick the smaller one
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            # Move current pointer forward
            current = current.next

        # If any list has remaining nodes, append them
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return dummy.next


# Helper to create and test
def create_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# Test it
list1 = create_list([1, 2, 4])
list2 = create_list([1, 3, 4])
solution = Solution()
merged = solution.mergeTwoLists(list1, list2)
print(print_list(merged))  # Output: [1, 1, 2, 3, 4, 4]