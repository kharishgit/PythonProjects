class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # lst1=self.list1
        # lst2 = self.list2
        lst3 = sorted(list1+list2)
        return lst3