class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        clone_map = {}
        def dfs(original):
            if original in clone_map:
                return clone_map[original]
            cloned_node = Node(original.val)
            clone_map[original] = cloned_node
            for neighbor in original.neighbors:
                cloned_node.neighbors.append(dfs(neighbor))
            return cloned_node
        return dfs(node)

