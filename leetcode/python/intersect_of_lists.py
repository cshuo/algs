# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def len_list(h):
            lenth = 0
            while h is not None:
                lenth += 1
                h = h.next
            return lenth

        if headB is None or headA is None:
            return None
        alen = len_list(headA)
        blen = len_list(headB)
        while alen < blen:
            headB = headB.next
            blen -= 1
        while blen < alen:
            headA = headA.next
            alen -= 1

        while headA != headB:
            headA = headA.next
            headB = headB.next

        return headA


