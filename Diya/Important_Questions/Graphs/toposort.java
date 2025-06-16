import java.util.*;

public class TopoSortKahn {
    private int vertices;
    private List<List<Integer>> adjList;

    public TopoSortKahn(int vertices) {
        this.vertices = vertices;
        adjList = new ArrayList<>();
        for (int i = 0; i < vertices; i++) {
            adjList.add(new ArrayList<>());
        }
    }

    // Add a directed edge from u to v
    public void addEdge(int u, int v) {
        adjList.get(u).add(v);
    }

    // Topological Sort using Kahn's Algorithm (BFS)
    public void topologicalSort() {
        int[] inDegree = new int[vertices];

        // Step 1: Compute in-degrees
        for (int u = 0; u < vertices; u++) {
            for (int v : adjList.get(u)) {
                inDegree[v]++;
            }
        }

        // Step 2: Add all nodes with in-degree 0 to queue
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < vertices; i++) {
            if (inDegree[i] == 0)
                queue.offer(i);
        }

        // Step 3: Perform BFS
        List<Integer> topoOrder = new ArrayList<>();
        while (!queue.isEmpty()) {
            int u = queue.poll();
            topoOrder.add(u);

            for (int v : adjList.get(u)) {
                inDegree[v]--;
                if (inDegree[v] == 0)
                    queue.offer(v);
            }
        }

        // Step 4: Check for cycle
        if (topoOrder.size() != vertices) {
            System.out.println("Cycle detected! Topological sort not possible.");
        } else {
            System.out.println("Topological Sort (Kahn's Algorithm):");
            for (int node : topoOrder) {
                System.out.print(node + " ");
            }
        }
    }

    // Main method to test
    public static void main(String[] args) {
        TopoSortKahn graph = new TopoSortKahn(6);
        graph.addEdge(5, 2);
        graph.addEdge(5, 0);
        graph.addEdge(4, 0);
        graph.addEdge(4, 1);
        graph.addEdge(2, 3);
        graph.addEdge(3, 1);

        graph.topologicalSort();
    }
}


import java.util.*;

public class TopologicalSort {
    private int vertices; // Number of vertices
    private List<List<Integer>> adjList; // Adjacency list

    // Constructor
    public TopologicalSort(int vertices) {
        this.vertices = vertices;
        adjList = new ArrayList<>();
        for (int i = 0; i < vertices; i++)
            adjList.add(new ArrayList<>());
    }

    // Add edge from u to v
    public void addEdge(int u, int v) {
        adjList.get(u).add(v);
    }

    // DFS utility function
    private void dfs(int node, boolean[] visited, Stack<Integer> stack) {
        visited[node] = true;

        for (int neighbor : adjList.get(node)) {
            if (!visited[neighbor])
                dfs(neighbor, visited, stack);
        }

        stack.push(node); // Add to stack after visiting all neighbors
    }

    // Topological Sort function
    public void topologicalSort() {
        Stack<Integer> stack = new Stack<>();
        boolean[] visited = new boolean[vertices];

        for (int i = 0; i < vertices; i++) {
            if (!visited[i])
                dfs(i, visited, stack);
        }

        System.out.println("Topological Sort:");
        while (!stack.isEmpty()) {
            System.out.print(stack.pop() + " ");
        }
    }

    // Main method to test
    public static void main(String[] args) {
        TopologicalSort graph = new TopologicalSort(6);
        graph.addEdge(5, 2);
        graph.addEdge(5, 0);
        graph.addEdge(4, 0);
        graph.addEdge(4, 1);
        graph.addEdge(2, 3);
        graph.addEdge(3, 1);

        graph.topologicalSort();
    }
}
