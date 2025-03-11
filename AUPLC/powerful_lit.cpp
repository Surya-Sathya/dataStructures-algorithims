#include <unordered_map>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct TrieNode {
    vector<TrieNode*> present_arr;
    TrieNode(): present_arr(26, nullptr) {}
};

class Trie {
    TrieNode* head = new TrieNode;
public: 
    Trie() {}

    void insert(string word) {
        cout << 0;
        
    }
}

int main() {
    
}