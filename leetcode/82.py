class Solution(object):
    def deleteDuplicates(self, head):

        if not head or not head.next:
            return head

        dummy = ListNode()

        per = dummy

        cur = head

        while cur :
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            if per.next == cur:
                per = per.next
            else:
                per.next = cur.next
            cur = cur.next
        return dummy.next