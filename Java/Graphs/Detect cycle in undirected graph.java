import java.util.*;

public class Solution {
    private boolean dfs(int node, Queue<int[]> Q, int[] visited, ArrayList<ArrayList<Integer>> adjLs) {
        Q.offer(new int[]{node, -1});
        visited[node] = 1;

        while (!Q.isEmpty()) {
            int[] pair = Q.poll();
            int currentNode = pair[0];
            int parent = pair[1];

            for (int i : adjLs.get(currentNode)) {
                if (visited[i] == 0) {
                    Q.offer(new int[]{i, currentNode});
                    visited[i] = 1;
                } else if (parent != i) {
                    return true;
                }
            }
        }
        return false;
    }

    public static String cycleDetection(int[][] edges, int n, int m) {
        int[] visited = new int[n + 1];
        ArrayList<ArrayList<Integer>> adjLs = new ArrayList<>();

        for (int i = 0; i <= n; i++) {
            adjLs.add(new ArrayList<>());
        }

        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            adjLs.get(u).add(v);
            adjLs.get(v).add(u);
        }

        Solution solution = new Solution();
        Queue<int[]> Q = new LinkedList<>();
        for (int i = 1; i <= n; i++) {
            if (visited[i] == 0) {
                if (solution.dfs(i, Q, visited, adjLs)) {
                    return "Yes";
                }
            }
        }
        return "No";
    }
}
