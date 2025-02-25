class MyCircularDeque:
 class Node:
  def __init__(self,val=0,next=None,prev=None):
   self.val=val
   self.next=next
   self.prev=prev
 def __init__(self,k):
  self.k=k
  self.size=0
  self.head=self.Node(-1)
  self.tail=self.Node(-1)
  self.head.next=self.tail
  self.tail.prev=self.head
 def insertFront(self,value):
  if self.isFull():
   return False
  node=self.Node(value)
  node.next=self.head.next
  node.prev=self.head
  self.head.next.prev=node
  self.head.next=node
  self.size+=1
  return True
 def insertLast(self,value):
  if self.isFull():
   return False
  node=self.Node(value)
  node.next=self.tail
  node.prev=self.tail.prev
  self.tail.prev.next=node
  self.tail.prev=node
  self.size+=1
  return True
 def deleteFront(self):
  if self.isEmpty():
   return False
  self.head.next=self.head.next.next
  self.head.next.prev=self.head
  self.size-=1
  return True
 def deleteLast(self):
  if self.isEmpty():
   return False
  self.tail.prev=self.tail.prev.prev
  self.tail.prev.next=self.tail
  self.size-=1
  return True
 def getFront(self):
  return -1 if self.isEmpty() else self.head.next.val
 def getRear(self):
  return -1 if self.isEmpty() else self.tail.prev.val
 def isEmpty(self):
  return self.size==0
 def isFull(self):
  return self.size==self.k