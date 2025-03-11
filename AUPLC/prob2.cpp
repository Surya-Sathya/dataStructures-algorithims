#include <unordered_map>
#include <iostream>
#include <string>
#include <vector>
#include <climits>
using namespace std;

int main() {
    int t;
    cin >> t;

    vector<int> vals(101, 1);
    vals[0] = -1;
    for(int i = 0; i < t; i++) {
        int a;
        cin >> a;
        string s;
        cin >> s;
        
        if(s == "No") {
            for(int j = 1; j < vals.size(); j++) {
                if(j % a == 0) vals[j] = 0;
            }
        }

        else {
            for(int j = 1; j < vals.size(); j++) {
                if(j % a != 0) vals[j] = 0;
            }
        }
    }   

    for(int j = 1; j < vals.size(); j++) {
        if(vals[j] == 1) cout << j;
    }

    return 0;
}