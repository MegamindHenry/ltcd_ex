# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        add_one = False
        val1 = L1.val
        val2 = L2.val
        d_sum = val1 + val2
        if d_sum > 9:
            d_sum -= 10
            add_one = True
        r = ListNode(d_sum, None)
        c1 = L1.next
        c2 = L2.next
        rc = r
        while c1 or c2:
            val1 = 0
            val2 = 0
            if c1:
                val1 = c1.val
                c1 = c1.next
            if c2:
                val2 = c2.val
                c2 = c2.next
            d_sum = val1 + val2
            if add_one:
                d_sum += 1
                add_one = False
            if d_sum > 9:
                d_sum -= 10
                add_one = True
            rn = ListNode(d_sum, None)
            rc.next = rn
            rc = rn
        if add_one:
            rn = ListNode(1, None)
            rc.next = rn
        return r


L13 = ListNode(9,None)
L12 = ListNode(8,L13)
L1 = ListNode(7,L12)

L23 = ListNode(9,None)
L22 = ListNode(8,L23)
L2 = ListNode(7,L22)

s = Solution()
r = s.addTwoNumbers(L1,L2)
print(r.val)
print(r.next.val)
print(r.next.next.val)
print(r.next.next.next.val)