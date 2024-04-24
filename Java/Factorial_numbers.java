import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static List<Long> helper(long n, long i , long fact, List<Long> res){
        if(fact <= n){
            res.add(fact);
            helper(n, i+1, fact*(i+1), res);
        }
        return res;
    }
    public static List<Long> factorialNumbers(long n) {
        List<Long> res = new ArrayList<>();
        return helper(n, 1, 1, res);
    }
}
