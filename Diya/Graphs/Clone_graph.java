class Solution {
    public Node cloneGraph(Node node) {
        if (node == null) {
            return null;
        }

        // Map to track visited nodes and their clones
        HashMap<Node, Node> visited = new HashMap<>();

        // Perform DFS to clone the graph
        cloneNode(node, visited);

        // Return the clone of the original node
        return visited.get(node);
    }

    private void cloneNode(Node node, HashMap<Node, Node> visited) {
        // Create a clone for the current node
        Node clonedNode = new Node(node.val);
        visited.put(node, clonedNode);

        // Traverse neighbors
        for (Node neighbor : node.neighbors) {
            // If the neighbor is not visited, clone it recursively
            if (!visited.containsKey(neighbor)) {
                cloneNode(neighbor, visited);
            }
            // Add the cloned neighbor to the current cloned node
            visited.get(node).neighbors.add(visited.get(neighbor));
        }
    }
}
