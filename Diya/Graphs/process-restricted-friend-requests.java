class Solution {
    int[] parent ; 
    int[] rank ; 
    public boolean[] friendRequests(int n, int[][] restrictions, int[][] requests) {
        boolean[] ans = new boolean[requests.length];
        int count = 0 ;
        init(n);
        for(int[] req : requests){
            int u = req[0];
            int v = req[1];
            boolean canBeFrnd = true ;

            int[] backupParent = Arrays.copyOf(parent , parent.length);
            int[] backupRank = Arrays.copyOf(rank , n);

            union(u , v);
            for(int[] res : restrictions){
                int U = res[0];
                int V = res[1];
                if(find(U) == find(V)){
                    canBeFrnd = false ;
                    break ;
                }
            }
            if(canBeFrnd){
                ans[count] = true ;
            }else{
                ans[count] = false ;
                parent = Arrays.copyOf(backupParent , n);
                rank = Arrays.copyOf(backupRank , n);
            }
            count++ ;
        }
        return ans;
    }
    public void init(int n){
        parent = new int[n];
        rank = new int[n];
        for(int i = 0 ; i < n ; i++) parent[i] = i ;
    }
    public int find(int x){
        if(parent[x] == x){
            return x ;
        }
        return parent[x] = find(parent[x]);
    }
    public void union(int u , int v){
        int parU = find(u);
        int parV = find(v);
        if(rank[parU] == rank[parV]){
            parent[parU] = parV ; 
            rank[parV]++ ;
        }else if(rank[parU] > rank[parV]){
            parent[parV] = parU ;
        }else{
            parent[parU] = parV ;
        }
    }
    
}