class Solution {
    public int matchPlayersAndTrainers(int[] players, int[] trainers) {
        CountDownLatch latch = new CountDownLatch(2);

        Thread.startVirtualThread(() -> {
            Arrays.sort(players);
            latch.countDown();
        });
        Thread.startVirtualThread(() -> {
            Arrays.sort(trainers);
            latch.countDown();
        });

        try {
            latch.await();
        } catch (Exception e) {

        }


        int i = 0, j = 0;
        int n = players.length, m = trainers.length;
        while (i < n && j < m) {
            if (players[i] <= trainers[j]) {
                i++;
            }
            j++;
        }
        return i;
    }
}