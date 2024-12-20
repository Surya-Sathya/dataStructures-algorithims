#include <iostream>

int main() {
    int a = 7; 
    int b = 21;
    int* p = &a;

    std::cout << "The deferenced value of our pointer will be: " << *p << std::endl; 

    p = &b; 
    std::cout << "After changing what memory address p points to, the deferenced value of our pointer will be: " << *p << std::endl; 

    //Example of what an unitialised variable looks like
    int c; 
    std::cout << c << "\n"; 

    //The pointer has freedom to point to other variables, the reference is assigned one time and becomes a reference to that
    //in memory, its not a COPY, its literally the address the previous variable points to 
    //ref = 7, a = 7 at memory location 0xA
    int& ref = a;
    p = &ref;
    std::cout << "After creating a reference/alias for variable 'a', the deferenced value of our pointer will be: " << *p << std::endl; 

    return 0;
}