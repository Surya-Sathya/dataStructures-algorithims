#include <iostream>
unsigned long long globalMemoize[100]; //why?? 


//O(n^2) Complexity -> Upper Bound (how many subsets of {1, 2, 3, ...k}?)
unsigned long long nonDynamicFib (int n) {
    if (n == 0) {
        return 0;
    }

    if (n == 1) {
        return 1;
    }

    int fib = nonDynamicFib(n-2) + nonDynamicFib(n-1);
    return fib;
};

//Memoization - Top down approach
unsigned long long dynamicFib (int n) {
    if (n<=1) {
        return n; 
    }
        if (globalMemoize[n] != -1) {
        return globalMemoize[n]; 
    }
    globalMemoize[n] = dynamicFib(n-2) + dynamicFib(n-1);
    return globalMemoize[n];
}


int main() {
    for (int i=0; i<51; i++) {
        globalMemoize[i] = -1;
    }

    int n; 
    unsigned long long int result = dynamicFib(30);    
    // unsigned long long result = nonDynamicFib(50);   
    std::cout << result; 
}