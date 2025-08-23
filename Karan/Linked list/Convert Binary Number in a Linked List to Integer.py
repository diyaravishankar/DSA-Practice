class ListNode:
 def __init__(self, val=0, next=None):
  self.val = val
  self.next = next
class Solution:
 def getDecimalValue(self, head):
  result = 0
  while head:
   result = (result << 1) | head.val
   head = head.next
  return result
head = ListNode(1, ListNode(0, ListNode(1)))
sol = Solution()
print(sol.getDecimalValue(head))