import java.util.*;

public class PrimMST {
    static class Edge {
        int dest, weight;
        Edge(int d, int w) { dest = d; weight = w; }
    }

    static class Node implements Comparable<Node> {
        int vertex, key;
        Node(int v, int k) { vertex = v; key = k; }

        public int compareTo(Node other) {
            return this.key - other.key;
        }
    }

    public static void primMST(List<List<Edge>> graph, int V) {
        boolean[] inMST = new boolean[V];
        int[] key = new int[V];           // Cost to reach node
        int[] parent = new int[V];        // MST parent tracking

        Arrays.fill(key, Integer.MAX_VALUE);
        Arrays.fill(parent, -1);
        key[0] = 0;

        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(0, 0));

        int mstWeight = 0;

        while (!pq.isEmpty()) {
            Node node = pq.poll();
            int u = node.vertex;

            if (inMST[u]) continue;
            inMST[u] = true;
            mstWeight += node.key;

            for (Edge edge : graph.get(u)) {
                int v = edge.dest;
                if (!inMST[v] && edge.weight < key[v]) {
                    key[v] = edge.weight;
                    pq.add(new Node(v, key[v]));
                    parent[v] = u;
                }
            }
        }

        System.out.println("Minimum Spanning Tree weight = " + mstWeight);
        for (int i = 1; i < V; i++) {
            System.out.println(parent[i] + " - " + i + " : " + key[i]);
        }
    }

    public static void main(String[] args) {
        int V = 5;
        List<List<Edge>> graph = new ArrayList<>();
        for (int i = 0; i < V; i++) graph.add(new ArrayList<>());

        graph.get(0).add(new Edge(1, 2));
        graph.get(0).add(new Edge(3, 6));
        graph.get(1).add(new Edge(0, 2));
        graph.get(1).add(new Edge(2, 3));
        graph.get(1).add(new Edge(3, 8));
        graph.get(1).add(new Edge(4, 5));
        graph.get(2).add(new Edge(1, 3));
        graph.get(2).add(new Edge(4, 7));
        graph.get(3).add(new Edge(0, 6));
        graph.get(3).add(new Edge(1, 8));
        graph.get(4).add(new Edge(1, 5));
        graph.get(4).add(new Edge(2, 7));

        primMST(graph, V);
    }
}
