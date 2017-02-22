class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        @doc: Time O(N), Space O(1). Store results in l2.
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        h = l2
        tail = None
        carry = 0
        while True:
            print "carry", carry
            if l1 and l2:
                tmp = l2.val
                l2.val = (l1.val + l2.val + carry) % 10
                carry = (l1.val + tmp + carry) / 10
            elif not l1 and not l2:
                if carry:
                    added = ListNode(carry)
                    tail.next = added
                break
            elif not l1:
                if carry:
                    tmp = l2.val
                    l2.val = (carry + l2.val) % 10
                    carry = (carry + tmp) / 10
            elif not l2:
                added = ListNode((carry + l1.val) % 10)
                carry = (carry + l1.val) / 10
                tail.next = added
                tail = added

            if l2 and not l2.next:
                tail = l2

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return h
