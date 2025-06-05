public class EggDroppingTabulation {

    public static int eggDrop(int e, int f) {
        int[][] dp = new int[e + 1][f + 1];

        // Base cases
        for (int i = 1; i <= e; i++) {
            dp[i][0] = 0;  // 0 floor = 0 trials
            dp[i][1] = 1;  // 1 floor = 1 trial
        }

        for (int j = 1; j <= f; j++) {
            dp[1][j] = j;  // 1 egg = j trials (linear search)
        }

        // Fill the rest of the table
        for (int i = 2; i <= e; i++) {
            for (int j = 2; j <= f; j++) {
                dp[i][j] = Integer.MAX_VALUE;

                for (int x = 1; x <= j; x++) {
                    int breakCase = dp[i - 1][x - 1];
                    int surviveCase = dp[i][j - x];
                    int worst = 1 + Math.max(breakCase, surviveCase);

                    dp[i][j] = Math.min(dp[i][j], worst);
                }
            }
        }

        return dp[e][f];
    }

    public static void main(String[] args) {
        int eggs = 2, floors = 10;
        System.out.println("Minimum number of attempts: " + eggDrop(eggs, floors));
    }
}
