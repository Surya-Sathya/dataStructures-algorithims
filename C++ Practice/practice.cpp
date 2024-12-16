#include <iostream>

//C++ provides you a different view of programming; a better understanding of hardware you can take into any language

int main() {
    //We can't actually find the size of this array, we can't append elements because memory is "carved in stone"
    //We can't increase the size of the memory allocated to the program code/variables
    //C++ doesn't store extra information, it wasn't to store least amount of space possible, hence no len() function

    //Length of array
    int my_array[100]; 

    my_array[0] = 50;
    my_array[1] = 100;
    my_array[2] = 150;

    int array_len = 3; 

    array_len++;
    my_array[array_len-1] = 200;

    for(int i = 0; i < )

    return 0; 
}