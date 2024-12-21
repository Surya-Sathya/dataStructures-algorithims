#include <vector>
#include <iostream>
using namespace std; 

class Solution {
public:
    int countPrimes(int n) {
        //When the keys are strings, custom objects, or other non-integer data types, 
        //unordered_map provides an efficient way to associate keys with values. -> ik you want to use a hashmap, but don't
        //collisions + overhead -> vectors you can find with indicies easily -> don't know size of dataset/dataset is sparse
        //non-copntiguous IDs (such as id 101, and id 202, but you don't want extra space), deleting stuff quickly without resizing
        int num_primes = 0;
        //vector<type> v(n, val); --> better cache locality, lower chances of cache misses, data stored contiguously in memory
        //underlying structure for hashmap is mostly empty array, but hash table values not stored contiguously, worse cache locality
        vector<int> umap(n, true); 

        if(n>1) umap[0] = umap[1] = 0; 

        for(int i=2; i<n; i++) {
            if(umap[i]) {
                //cout << "i: " << i << "\n"; 
                num_primes++;

                for(int composite = i*2; composite < n; composite += i) {
                    //cout << "j: " << j << "\n"; 
                    umap[composite] = 0;
                }
            }
        } 
        return num_primes;
        //"In particular, arrays/vectors are contiguous memory blocks, so large chunks of them will be loaded into the cache upon first access. This makes it comparatively quick to access future elements of the array. Linked lists on the other hand aren't necessarily in contiguous blocks of memory, and could lead to more cache misses, which increases the time it takes to access them."
    }
};

/*
If we wanted to loop through this array, the first access to ffff 0000 would require us to go to memory to retrieve (a very slow operation in CPU cycles). However, after the first access the rest of the array would be in the cache, and subsequent accesses would be much quicker. With the linked list, the first access to ffff 1000 would also require us to go to memory. Unfortunately, the processor will cache the memory directly surrounding this location, say all the way up to ffff 2000. As you can see, this doesn't actually capture any of the other elements of the list, which means that when we go to access l_data->next, we will again have to go to memory.

Cache locality refers to the likelihood of successive operations being in the cache and thus being faster. In an array, you maximize the chances of sequential element access being in the cache.
Address      Contents       | Address      Contents
ffff 0000    data[0]        | ffff 1000    l_data
ffff 0040    data[1]        |   ....
ffff 0080    data[2]        | ffff 3460    l_data->next
ffff 00c0    data[3]        |   ....
ffff 0100    data[4]        | ffff 8dc0    l_data->next->next
                            | ffff 8e00    l_data->next->next->next
                            |   ....
                            | ffff 8f00    l_data->next->next->next->next
*/