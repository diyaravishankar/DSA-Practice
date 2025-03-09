class Solution {
    longestDiverseString(a, b, c) 
    {let maxHeap = [];
    for (let [char, count] of [['a', a], ['b', b], ['c', c]]) {
        if (count > 0) maxHeap.push([count, char]);}
        maxHeap.sort((x, y) => y[0] - x[0]);
        let result = '';
        while (maxHeap.length) 
        {let [count1, char1] = maxHeap.shift();
        if (result.endsWith(char1 + char1)) {
            if (!maxHeap.length) break;
            let [count2, char2] = maxHeap.shift();
            result += char2;
            if (--count2 > 0) maxHeap.push([count2, char2]);
            maxHeap.push([count1, char1]);
            } else {let useCount = count1 >= 2 ? 2 : 1;
            result += char1.repeat(useCount);
            count1 -= useCount;if (count1 > 0) maxHeap.push([count1, char1]);
            }maxHeap.sort((x, y) => y[0] - x[0]);
            }return result;
            }}  
const sol = new Solution();  
const longestDiverseString = (a, b, c) => sol.longestDiverseString(a, b, c);  
console.log(longestDiverseString(1, 1, 7));  
console.log(longestDiverseString(7, 1, 0));