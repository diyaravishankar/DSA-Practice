public class DSU {
    int[] parent;
    int[] rank;

    // Constructor to initialize n elements (0 to n-1)
    public DSU(int n) {
        parent = new int[n];
        rank = new int[n];

        // Initially, each element is its own parent (single node set)
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            rank[i] = 0; // Optional, can also use size instead
        }
    }

    // Find with path compression
    public int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]); // path compression
        }
        return parent[x];
    }

    // Union by rank
    public void union(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);

        // If already in the same set
        if (rootX == rootY) return;

        // Union by rank
        if (rank[rootX] < rank[rootY]) {
            parent[rootX] = rootY;
        } else if (rank[rootX] > rank[rootY]) {
            parent[rootY] = rootX;
        } else {
            parent[rootY] = rootX;
            rank[rootX]++;
        }
    }

    // Check if two elements are in the same set
    public boolean isConnected(int x, int y) {
        return find(x) == find(y);
    }
}


class GfG {

    int find(int parent[], int i) {
        if (parent[i] == i) {
            return i;
        }
      
        // Else recursively find the representative
        // of the parent 
        return find(parent,parent[i]);
    }

    void unionSet(int parent[], int i, int j) {
        int irep = find(parent,i);

        // Representative of set containing j
        int jrep = find(parent,j);

        // Make the representative of i's set be 
        // the representative of j's set
        parent[irep] = jrep;
    }
}