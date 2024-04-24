#include<vector>
using namespace std;
int getLongestZeroSumSubarrayLength(vector<int> &arr){
	unordered_map <int, int> hmap;
	int sum = 0, maxLen = 0;

	for(int i = 0; i < arr.size(); ++i){
		sum += arr[i];

                if (sum == 0) {
                  maxLen = max(maxLen, i + 1);
                } 
				else if (hmap.find(sum) != hmap.end()) {
                  maxLen = std::max(maxLen, i - hmap[sum]);
                } else {
                  hmap[sum] = i;
			}
        }
	return maxLen;
	
}
