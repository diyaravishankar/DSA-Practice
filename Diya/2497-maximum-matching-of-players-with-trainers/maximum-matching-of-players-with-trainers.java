class Solution {
    public int matchPlayersAndTrainers(int[] players, int[] trainers) {
        sort(players,0,players.length-1);
        sort(trainers,0,trainers.length-1);
        int matchings=0;
        int i=0,j=0;
        while(i<players.length && j<trainers.length){
            if(players[i]<=trainers[j]){
                matchings++;
                j++;
            }
            i++;
        }
        return matchings;
    }
    void sort(int[] nums,int s,int e){
        if(s==e){
            return;
        }
        int m=s+(e-s)/2;
        sort(nums,s,m);
        sort(nums,m+1,e);
        conquer(nums,s,m,e);
    }
    void conquer(int[] nums,int s,int m,int e){
        int[] mix=new int[e-s+1];
        int i=s,j=m+1,k=0;
        while(i<=m && j<=e){
            mix[k++]=nums[i]>nums[j]?nums[i++]:nums[j++];
        }
        while(i<=m){
            mix[k++]=nums[i++];
        }
        while(j<=e){
            mix[k++]=nums[j++];
        }
        for(int a=0;a<mix.length;a++){
            nums[a+s]=mix[a];
        }
    }
}