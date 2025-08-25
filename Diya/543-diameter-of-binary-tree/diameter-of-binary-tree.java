/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    static class TreeInfo {
        int ht, diam;
        TreeInfo(int ht, int diam) {
            this.ht = ht;
            this.diam = diam;
        }
    }
    
    public int diameterOfBinaryTree(TreeNode root) {
        return diameter(root).diam;
    }

    private TreeInfo diameter(TreeNode root) {
        if (root == null) {
            return new TreeInfo(0, 0);
        }
        
        TreeInfo left = diameter(root.left);
        TreeInfo right = diameter(root.right);
        
        int height = Math.max(left.ht, right.ht) + 1;
        
        int diam1 = left.diam;
        int diam2 = right.diam;
        int diam3 = left.ht + right.ht; // diameter is edge count, so no +1
        
        int diam = Math.max(diam1, Math.max(diam2, diam3));
        
        return new TreeInfo(height, diam);
    }
}
