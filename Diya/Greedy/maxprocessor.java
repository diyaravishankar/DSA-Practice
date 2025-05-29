import java.util.Collections;
class Solution {
     public int minProcessingTime(List<Integer> processorTime, List<Integer> tasks) {
        Collections.sort(tasks, Collections.reverseOrder()); 
        Collections.sort(processorTime);

        int maxTime = 0;
        int taskIndex = 0;

        for (int i = 0; i < processorTime.size(); i++) {
            int currentMax = 0;
            for (int j = 0; j < 4; j++) {
                currentMax = Math.max(currentMax, processorTime.get(i) + tasks.get(taskIndex++));
            }
            maxTime = Math.max(maxTime, currentMax);
        }

        return maxTime;
    }

}