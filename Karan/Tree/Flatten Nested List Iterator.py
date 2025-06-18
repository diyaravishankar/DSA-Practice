class NestedIterator:
 def __init__(self, nestedList):
  self.stack = []
  self._pushList(nestedList)
 def _pushList(self, nestedList):
  for i in range(len(nestedList) - 1, -1, -1):
   self.stack.append(nestedList[i])
 def next(self):
  return self.stack.pop().getInteger()
 def hasNext(self):
  while self.stack:
   top = self.stack[-1]
   if top.isInteger():
    return True
   self.stack.pop()
   self._pushList(top.getList())
  return False