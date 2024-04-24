using namespace std;
vector<long long> helper(long long n, long long i, long long fact, vector<long long> res){
    if(fact <= n){
        res.push_back(fact);
        return helper(n, i+1, fact * (i+1), res);
    }
    return res;



}
vector<long long> factorialNumbers(long long n) {
    vector<long long > res;
    return helper(n, 1, 1, res);
}
