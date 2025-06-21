import java.util.*;

public class KruskalMST {
    static class Edge implements Comparable<Edge> {
        int src, dest, weight;
        Edge(int s, int d, int w) { src = s; dest = d; weight = w; }

        public int compareTo(Edge other) {
            return this.weight - other.weight;
        }
    }

    static class UnionFind {
        int[] parent, rank;

        UnionFind(int n) {
            parent = new int[n];
            rank = new int[n];
            for (int i = 0; i < n; i++) parent[i] = i;
        }

        int find(int u) {
            if (u != parent[u])
                parent[u] = find(parent[u]);
            return parent[u];
        }

        boolean union(int u, int v) {
            int rootU = find(u), rootV = find(v);
            if (rootU == rootV) return false;
            if (rank[rootU] < rank[rootV]) parent[rootU] = rootV;
            else if (rank[rootU] > rank[rootV]) parent[rootV] = rootU;
            else {
                parent[rootV] = rootU;
                rank[rootU]++;
            }
            return true;
        }
    }

    public static void kruskalMST(List<Edge> edges, int V) {
        Collections.sort(edges);
        UnionFind uf = new UnionFind(V);

        int mstWeight = 0;
        List<Edge> mst = new ArrayList<>();

        for (Edge e : edges) {
            if (uf.union(e.src, e.dest)) {
                mst.add(e);
                mstWeight += e.weight;
            }
        }

        System.out.println("Minimum Spanning Tree weight = " + mstWeight);
        for (Edge e : mst) {
            System.out.println(e.src + " - " + e.dest + " : " + e.weight);
        }
    }

    public static void main(String[] args) {
        int V = 6;
        List<Edge> edges = new ArrayList<>();
        edges.add(new Edge(0, 1, 4));
        edges.add(new Edge(0, 2, 4));
        edges.add(new Edge(1, 2, 2));
        edges.add(new Edge(1, 3, 5));
        edges.add(new Edge(2, 3, 5));
        edges.add(new Edge(2, 4, 11));
        edges.add(new Edge(3, 4, 2));
        edges.add(new Edge(3, 5, 1));
        edges.add(new Edge(4, 5, 7));

        kruskalMST(edges, V);
    }
}
