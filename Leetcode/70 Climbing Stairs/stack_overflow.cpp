#include <iostream> 
int ffunction(int n); 

int main() {
    
    ffunction(10);
}

int ffunction(int n) {
    std::cout << "Here" << "\n"; 
    return ffunction(n-1); 
}