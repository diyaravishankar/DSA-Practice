class Codec:
 def serialize(self, root):
  def preorder(node):
   if not node:
    return []
   return [str(node.val)] + preorder(node.left) + preorder(node.right)
  return ','.join(preorder(root))
 def deserialize(self, data):
  if not data:
   return None
  values = list(map(int, data.split(',')))
  index = [0]
  def build(lower, upper):
   if index[0] == len(values):
    return None
   val = values[index[0]]
   if val < lower or val > upper:
    return None
   index[0] += 1
   node = TreeNode(val)
   node.left = build(lower, val)
   node.right = build(val, upper)
   return node
  return build(float('-inf'), float('inf'))