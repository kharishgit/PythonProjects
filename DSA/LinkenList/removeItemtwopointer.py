class Listnode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

class Solution:
    def RemoveFromEnd(self, head, n):
        dummy = Listnode(0, head)
        left = dummy
        right = head
        while n > 0 and right:
            right = right.next
            n-=1
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next

def create_linked_list(arr):
    dummy = Listnode(0)
    print("Dummy", type(dummy))
    current = dummy
    for val in arr:
        current.next = Listnode(val)
        current = current.next
    return dummy.next

# Helper function to print linked list
def print_linked_list(head):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" -> ".join(result))

# Example usage
head = create_linked_list([1, 2, 3, 4, 5])
n = 2

sol = Solution()
new_head = sol.RemoveFromEnd(head, n)

print("Linked list after removing", n, "node(s) from end:")
print_linked_list(new_head)