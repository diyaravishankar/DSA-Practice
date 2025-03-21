class Solution:
    def treeQueries(self, root: TreeNode, queries: List[int]) -> List[int]:
        from collections import defaultdict
        depth = {}
        height = {}
        level_max = defaultdict(list)
        def dfs1(node, d):
            if not node:
                return -1
            depth[node.val] = d
            left_h = dfs1(node.left, d + 1)
            right_h = dfs1(node.right, d + 1)
            h = max(left_h, right_h) + 1
            height[node.val] = h
            level_max[d].append(h)
            return h
        dfs1(root, 0)
        for lvl in level_max:
            level_max[lvl].sort(reverse=True)
        res = []
        for q in queries:
            d = depth[q]
            h = height[q]
            if len(level_max[d]) == 1:
                res.append(d - 1)
            else:
                max_h = level_max[d][1] if level_max[d][0] == h else level_max[d][0]
                res.append(d + max_h)
        return res