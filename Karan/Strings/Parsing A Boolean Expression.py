class Solution:
 def parseBoolExpr(self,expression:str)->bool:
  stack=[]
  for ch in expression:
   if ch==")":
    values=set()
    while stack[-1]!="(":
     values.add(stack.pop())
    stack.pop()
    op=stack.pop()
    if op=="!":stack.append("t" if "f" in values else "f")
    elif op=="&":stack.append("t" if "f" not in values else "f")
    elif op=="|":stack.append("t" if "t" in values else "f")
   elif ch!=",":
    stack.append(ch)
  return stack[0]=="t"