import java.util.HashMap;

public class Solution {
    public static int getLongestZeroSumSubarrayLength(int []arr){
        HashMap<Integer, Integer> hmap = new HashMap<>();
        int sum = 0;
        int max_len = 0;

        for(int i = 0; i < arr.length; i++){
            sum += arr[i];

            if (sum == 0){
                max_len = Math.max(max_len, i+1);
            }
            else if(hmap.containsKey(sum)){
                max_len = Math.max(max_len, i - hmap.get(sum));
            }
            else{
                hmap.put(sum, i);
            }
        }
        return max_len;
    }
}
