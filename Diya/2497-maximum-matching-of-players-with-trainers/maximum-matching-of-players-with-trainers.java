class Solution {
    public int matchPlayersAndTrainers(int[] players, int[] trainers) {

        Thread t1 = new Thread(()->Arrays.sort(players));
        Thread t2 = new Thread(()->Arrays.sort(trainers));
        t1.start();
        t2.start();
        try{
            t1.join();
            t2.join();
        }catch(Exception e){}

        //Arrays.sort(players);
        //Arrays.sort(trainers);

        int matches = 0;
        int playPtr = 0, trainPtr = 0;
        while(trainPtr < trainers.length && playPtr < players.length) {
            if ( players[playPtr] <= trainers[trainPtr]) {
                playPtr++; trainPtr++; matches++;
            }
            else trainPtr++;   
        }

        return matches;
    }
}