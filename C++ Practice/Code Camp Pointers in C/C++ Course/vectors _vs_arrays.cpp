#include <iostream>
#include <vector>

std::vector<int> reverse_vec(std::vector<int>& vec) {
    int i; 
    std::vector<int> reversed;  
    for(i = vec.size()-1; i > -1; i--) {
        reversed.push_back(vec[i]); 
    }

    return reversed; 
}

int main() {
    //Initialise Array -> Fixes sequence of elements while Vectors offer dyanmic sizing and flexibility (size operator for instance)
    //Vectors: vec.push(back), vec.size(), vec.pop_back(), vec.insert(), we can only return dynamically allocated vectors, not array
    //sort(vec.begin(), vec.end()); to sort using STL, Standard Template Library
    int i; 
    std::vector<int> vec = {4, 3, 2, 1};  

    vec = reverse_vec(vec); 

    std::cout << "{"; 
    for(i=0; i<vec.size(); i++) {
        std::cout << vec[i] << ", "; 
    }
    std::cout << "}"; 

    return 0;
}