#include <iostream>

void sum_function(int& x, int& y){
    //int& is a REFERENCE, i.e. the machine address of a. 
    x += 1;
    y += 1; 
}

void sum_function_with_pointer_type(int* n, int* m){
    *n += 1;
    *m += 1; 
}

int main(){
    //Local variables
    int a = 5;
    int b = 10; 

    //sum_function(a, b); --> this is a call by value, where a maps to x (a -> x), doesn't changle local a
    sum_function(a, b); //Here we use the alias' x and y, &a and &x are the same address -> pass by reference
    sum_function_with_pointer_type(&a, &b); 
    std::cout << "a: " << a << ", wheras b: " << b << std::endl; 

    int* p = &a;

    //Dereferencing pointer
    std::cout << *p << ", with the pointer have an address of:" << &p << ", which points to the address" << p << std::endl; 
    std::cout << "Before adding 1: " << p << ", after adding 1: " << ++p << std::endl; 
}