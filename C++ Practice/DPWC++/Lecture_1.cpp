#include <iostream>

int main() {
    /*
    Topics => Memory management, arrays, why we can't find size of arrays, pointers, arrays to pointers


    Memory Management: Why can't we know the size of arrays?
    -Everything we know has a size an array has a size; for RAM we can have as much memory as want until 16gb
    -Instance of GuessTheNumber.exe will use some memory; in the form of 4 byte ints, to the program code
    -When a program is compiled, its layout is "carved in stone" -> you cannot make it bigger or anything
    -To add an element, you would have to break the array memory location and place another element inside 
    -Keeping track of the size of the array is extra memory, which we don't want
    */

    //Static memory allocation -> Key technique to add/find len, but you do have to know the max size of the array
    //These allow for memory savings, you can put an upper limit to it; perfect for embedded systems, not resizing arrays you never resize
    int myArray[100]; 
    int arrayLen = 3;

    myArray[0] = 30;
    myArray[1] = 40;
    myArray[2] = 50;

    //Increase array:
    myArray[arrayLen++] = 70;
    myArray[arrayLen++] = 80;

    std::cout << arrayLen << "\n"; 

    for(int i = 0; i<arrayLen; i++){
        std::cout << myArray[i] << " "; 
    }
    std::cout << "\n";


    //The other solution -> Dynamic memory allocation; but we take a detour with pointers/addresses:
    int* p = &arrayLen;
    *p = 10; 
    std::cout<<*p<<"\n"; 
    std::cout<<"In order to represent the address of your variable array length " << arrayLen <<", use the & operator to get: " << &arrayLen << "\n"; 

    int* arraypointer = myArray; //Arrays are just pointers
    std::cout<<*arraypointer<< " " << *(arraypointer +1) << " " << myArray[0] << " " << myArray[1]; 
    
    return 0; 
}