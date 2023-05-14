# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result = None
        add_next_digit = False
        cur1, cur2 = l1, l2

        while 1:
            sumv = cur1.val + cur2.val

            if add_next_digit:
                add_next_digit = False
                sumv += 1

            if sumv >= 10:
                add_next_digit = True
                sumv -= 10

            if not result:
                result = ListNode(sumv)
            else:
                cur_res = result
                while cur_res.next:
                    cur_res = cur_res.next
                cur_res.next = ListNode(sumv)

            if not cur1.next and not cur2.next:
                break
            cur1, cur2 = cur1.next or ListNode(), cur2.next or ListNode()

        if add_next_digit:
            cur_res = result
            while cur_res.next:
                cur_res = cur_res.next
            cur_res.next = ListNode(1)

        return result
