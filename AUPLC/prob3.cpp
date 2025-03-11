#include <iostream>
#include <vector>
using namespace std;

int main() {
    long long t;
    cin >> t;
    vector<int> res;

    for(int i = 0; i < t; i++) {
        long long n;
        cin >> n; 
        long long l = 1, r = 1e6;
        long long ans = 0;

        while (l <= r) {
            long long mid = l + (r - l) / 2;
            if ((mid * (mid + 1) * (mid + 2)) / 6 <= n) {
                ans = mid;
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }

        res.push_back(ans);
    }
    for(int a:res) cout << a << endl;
    return 0;
}
