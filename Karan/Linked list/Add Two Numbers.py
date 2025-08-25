class Solution:
    def addTwoNumbers(self,l1,l2):
        d=ListNode()
        c=0
        cur=d
        while l1 or l2 or c:
            v=c
            if l1:v+=l1.val;l1=l1.next
            if l2:v+=l2.val;l2=l2.next
            c=v//10
            cur.next=ListNode(v%10)
            cur=cur.next
        return d.next