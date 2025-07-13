class Solution {
    // public int minMatchIdx(int s, int e, int[] trainers, int target) {
    //     int ans = trainers.length;
    //     while (s <= e) {
    //         int m = s + (e - s) / 2;
    //         if (trainers[m] >= target) {
    //             ans = m;
    //             e = m - 1;
    //         } else {
    //             s = m + 1;
    //         }
    //     }
    //     return ans;
    // }

    // public int matchPlayersAndTrainers(int[] players, int[] trainers) {
    //     Arrays.sort(players);
    //     Arrays.sort(trainers);
    //     int n = trainers.length;
    //     int s = 0;
    //     int e = n - 1;
    //     int maxMatch = 0;
    //     for (int p : players) {
    //         int idxMatchedWithCurrPlayer = minMatchIdx(s, e, trainers, p);
    //         if (idxMatchedWithCurrPlayer == n) {
    //             break;
    //         }
    //         s = idxMatchedWithCurrPlayer + 1;
    //         maxMatch++;
    //     }
    //     return maxMatch;
    // }

    public int matchPlayersAndTrainers(int[] players, int[] trainers) {
        int m = players.length;
        int n = trainers.length;

        Thread t1 = new Thread(() -> Arrays.sort(players));
        Thread t2 = new Thread(() -> Arrays.sort(trainers));
        t1.start();
        t2.start();
        try {
            t1.join();
            t2.join();
        } catch (Exception e) {
        }

        int left = 0;
        int right = 0;
        int count = 0;

        while (left < m && right < n) {
            if (trainers[right] >= players[left]) {
                count++;
                left++;
            }
            right++;
        }
        return count;
    }
}