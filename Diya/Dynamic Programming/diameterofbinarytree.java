class Solution {
    int res = Integer.MIN_VALUE;  

    int diameter(Node root) {
        solve(root);
        return res-1;
    }

    int solve(Node root) {
        if (root == null) {
            return 0;
        }
        int l = solve(root.left);
        int r = solve(root.right);

        // update the diameter (nodes on the path)
        res = Math.max(res, l + r + 1);

        // return the height
        return Math.max(l, r)+1;
    }
}
