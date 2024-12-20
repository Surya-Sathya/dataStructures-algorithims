#include <iostream>
#include <vector>

void change_var_to_10(int& var) {
    var = 10; 
}

int main() {
    //Here we explore references
    int x = 5; 
    std::cout << "Variable x was orginally " << x << std::endl;

    change_var_to_10(x); 

    std::cout << "Now it is " << x << std::endl; 
    std::cout << "This is the power of a reference, where we are actually changing x" << std::endl;
    std::cout << "A reference is not a pointer, nor a copy of the object, it IS the object" << std::endl; 
    
    
    //Here we explore vectors and arrays
    std::string cars[4] = {"Volvo", "BMW", "Rat", "Merc"}; 
    std::vector<std::string> carVector = {"Supercar", "Superat"};

    //Add two cars to the vector
    carVector.push_back("Volvo"); 
    carVector.push_back("To Delete"); 
    carVector.push_back("More to delete"); 

    for (int i = 0; i < carVector.size(); i++) {
        std::cout << carVector[i] << std::endl; 
    }

    carVector.pop_back(); 

    for (int i = 0; i < carVector.size(); i++) {
        std::cout << carVector[i] << "\n"; 
    }

    //Post Decrement VS Pre-Decrement 
    int accum = 10;
    int a = 10;
    bool equals_post = false; 
    bool equals_pre = false;

    if(a==accum++){equals_post = true;}
    if(a==++accum){equals_pre = true;}

    std::cout << equals_pre << "\n"; 

    return 0; 
}