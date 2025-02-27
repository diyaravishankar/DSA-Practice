class Solution {
    int canCompleteCircuit(int[] gas, int[] cost) {
    int total=0,tank=0,start=0;
    for(int i=0;i<gas.length;i++){
    total+=gas[i]-cost[i];
    tank+=gas[i]-cost[i];
    if(tank<0){
    start=i+1;
    tank=0;
    }
    }
    return total<0?-1:start;
    }
    public static void main(String[] args) {
    Solution sol=new Solution();
    System.out.println(sol.canCompleteCircuit(new int[]{1,2,3,4,5},new int[]{3,4,5,1,2}));
    System.out.println(sol.canCompleteCircuit(new int[]{2,3,4},new int[]{3,4,3}));
    }
    }