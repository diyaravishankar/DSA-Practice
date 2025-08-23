class TrieNode:
 def __init__(self):
  self.children = {}
  self.is_deleted = False
  self.name = ""
class Solution:
 def deleteDuplicateFolder(self, paths):
  def build_trie(paths):
   root = TrieNode()
   for path in paths:
    curr = root
    for folder in path:
     if folder not in curr.children:
      curr.children[folder] = TrieNode()
      curr.children[folder].name = folder
     curr = curr.children[folder]
   return root
  def serialize(node, lookup, duplicates):
   if not node.children:
    return ""
   serials = []
   for child_name in sorted(node.children):
    child = node.children[child_name]
    serial = serialize(child, lookup, duplicates)
    serials.append(f"{child_name}({serial})")
   subtree = "".join(serials)
   if subtree in lookup:
    duplicates.add(lookup[subtree])
    duplicates.add(node)
   else:
    lookup[subtree] = node
   return subtree
  def collect_paths(node, path, result):
   if node.is_deleted:
    return
   if node.name:
    path.append(node.name)
    result.append(path[:])
   for child in node.children.values():
    collect_paths(child, path, result)
   if node.name:
    path.pop()
  root = build_trie(paths)
  lookup = {}
  duplicates = set()
  serialize(root, lookup, duplicates)
  for node in duplicates:
   node.is_deleted = True
  result = []
  collect_paths(root, [], result)
  return result