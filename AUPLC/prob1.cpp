#include <unordered_map>
#include <iostream>
#include <string>
#include <vector>
#include <climits>
using namespace std;

int main() {
    int t;
    cin >> t;
    unordered_map<string,int> hmap;
    vector<string> hmap_key_vals;

    for(int i = 0; i < t; i++) {
        string s;
        cin >> s;
        hmap_key_vals.push_back(s);
    } 

    for(auto k : hmap_key_vals) hmap[k]++;

    pair<string, int> max_pair;
    max_pair.first = ' ';
    max_pair.second = INT_MIN;
    for(auto k : hmap) {
        if(k.second > max_pair.second) {
            max_pair.first = k.first;
            max_pair.second = k.second;
        }
        else if(k.second == max_pair.second) {
            if(k.first.size() < max_pair.first.size()) max_pair.first = k.first; 
        }
    }

    cout << max_pair.first;
    return 0;
}