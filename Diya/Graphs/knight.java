class Solution {
    static class Cell{
            int x,y,dist;
            Cell(int x,int y,int dist){
                int x=this.x;
                int y=this.y;
                int dist=this.dist;
            }
        }
    public int minStepToReachTarget(int knightPos[], int targetPos[], int n) {
        // Code here
        int []dx={-2,-1,1,2,2,1,-1,-2};
        int []dy={1,2,2,1,-1,-2,-2,-1};
        boolean [][]visited=new boolean[n+1][n+1];
        Queue<Cell> queue=new LinkedList<>();
        queue.add(new Cell(knightpos[0],knightpos[1],0));
        visited[knightpos[0]][[knightpos[1]]=true;
        while(!queue.isEmpty()){
            Cell curr=queue.poll();
            if(curr.x==targetPos[0]&&curr.y==targetPos[y]){
                return curr.dist;
            }            
            for(int i=1;i<8;i++){
                int nx=curr.dist+dx[i];
                int ny=curr.dist+dy[i];
                if(nx>=1 && ny>=1 && !visted[nx][ny]&&nx <= n && ny <= n){
                    visited[nx][ny]=true;
                    queue.add(new Cell(nx,ny,curr.dist+1));
                }
            }
        }
        return -1;
        
        
    }
}