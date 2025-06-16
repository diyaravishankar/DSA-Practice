import java.util.*;

public class TopologicalSortBFS {
    private int vertices;
    private List<List<Integer>> adjList;

    public TopologicalSortBFS(int vertices) {
        this.vertices = vertices;
        adjList = new ArrayList<>();
        for (int i = 0; i < vertices; i++)
            adjList.add(new ArrayList<>());
    }

    public void addEdge(int u, int v) {
        adjList.get(u).add(v);
    }

    public void topologicalSort() {
        int[] inDegree = new int[vertices];

        // Calculate in-degree for each vertex
        for (int u = 0; u < vertices; u++) {
            for (int v : adjList.get(u)) {
                inDegree[v]++;
            }
        }

        // Queue for vertices with in-degree 0
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < vertices; i++) {
            if (inDegree[i] == 0)
                queue.offer(i);
        }

        List<Integer> result = new ArrayList<>();

        while (!queue.isEmpty()) {
            int u = queue.poll();
            result.add(u);

            for (int v : adjList.get(u)) {
                inDegree[v]--;
                if (inDegree[v] == 0)
                    queue.offer(v);
            }
        }

        if (result.size() != vertices) {
            System.out.println("Graph has a cycle. Topological sort not possible.");
        } else {
            System.out.println("Topological Sort (BFS/Kahn's Algorithm):");
            for (int node : result)
                System.out.print(node + " ");
        }
    }

    public static void main(String[] args) {
        TopologicalSortBFS graph = new TopologicalSortBFS(6);
        graph.addEdge(5, 2);
        graph.addEdge(5, 0);
        graph.addEdge(4, 0);
        graph.addEdge(4, 1);
        graph.addEdge(2, 3);
        graph.addEdge(3, 1);

        graph.topologicalSort();
    }
}
