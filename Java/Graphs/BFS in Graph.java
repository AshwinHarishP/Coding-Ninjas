import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.LinkedList;
public class Solution {
    private void dfs(int node, int[] visited, Queue<Integer> Q,  List<List<Integer>> adj, ArrayList<Integer> res){
        visited[node] = 1;
        Q.add(node);
        while(!Q.isEmpty()){
            node = Q.poll();
            res.add(node);

            for(Integer i: adj.get(node)){
                if(visited[i] == 0){
                    Q.offer(i);
                    visited[i] = 1;
                }
            }
        }
    }
    public static List<Integer> bfsTraversal(int n, List<List<Integer>> adj){
        Solution solution = new Solution();
        int [] visited = new int[n];
        ArrayList<Integer> res = new ArrayList<>();
        Queue<Integer> Q = new LinkedList<>();
        
        solution.dfs(0, visited, Q, adj, res);
        return res;
    }
}

