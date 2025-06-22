import java.util.*;

public class GraphAnalysis {
    static int time = 0;
    static List<Integer>[] adj;
    static int[] disc, low, parent;
    static boolean[] visited;
    static Set<Integer> articulationPoints = new TreeSet<>();
    static List<int[]> bridges = new ArrayList<>();

    public static void dfs(int u) {
        visited[u] = true;
        disc[u] = low[u] = ++time;
        int children = 0;

        for (int v : adj[u]) {
            if (!visited[v]) {
                children++;
                parent[v] = u;
                dfs(v);

                low[u] = Math.min(low[u], low[v]);

                // Articulation point conditions
                if (parent[u] == -1 && children > 1)
                    articulationPoints.add(u);
                if (parent[u] != -1 && low[v] >= disc[u])
                    articulationPoints.add(u);

                // Bridge condition
                if (low[v] > disc[u]) {
                    if (u < v)
                        bridges.add(new int[]{u, v});
                    else
                        bridges.add(new int[]{v, u});
                }
            } else if (v != parent[u]) {
                low[u] = Math.min(low[u], disc[v]);
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(), M = sc.nextInt();

        adj = new ArrayList[N + 1];
        for (int i = 0; i <= N; i++)
            adj[i] = new ArrayList<>();

        for (int i = 0; i < M; i++) {
            int u = sc.nextInt(), v = sc.nextInt();
            adj[u].add(v);
            adj[v].add(u);
        }

        disc = new int[N + 1];
        low = new int[N + 1];
        parent = new int[N + 1];
        visited = new boolean[N + 1];
        Arrays.fill(parent, -1);

        for (int i = 1; i <= N; i++) {
            if (!visited[i]) {
                dfs(i);
            }
        }

        // Print articulation points
        System.out.println(articulationPoints.size());
        for (int ap : articulationPoints)
            System.out.print(ap + " ");
        System.out.println();

        // Sort and print bridges
        Collections.sort(bridges, (a, b) -> {
            if (a[0] != b[0]) return a[0] - b[0];
            return a[1] - b[1];
        });

        System.out.println(bridges.size());
        for (int[] bridge : bridges)
            System.out.println(bridge[0] + " " + bridge[1]);
    }
}
