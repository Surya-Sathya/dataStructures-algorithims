#include <iostream>

void merge(int merge_arr[], int leftHalf[], int leftsize, int rightHalf[], int rightsize) {
    int l=0, r=0, i=0;

    while (l < leftsize && r < rightsize) {
        if (leftHalf[l] <= rightHalf[r]) {
            merge_arr[i++] = leftHalf[l++];
        } else {
            merge_arr[i++] = rightHalf[r++];
        }
    }

    while (l < leftsize) {
        merge_arr[i++] = leftHalf[l++];
    }

    while (r < rightsize) {
        merge_arr[i++] = rightHalf[r++];
    }
}

void split(int merge_arr[], int merge_arr_size) {
    
    if (merge_arr_size <= 1) {
        return;
    }
    
    int leftsize = merge_arr_size / 2;
    int rightsize = (merge_arr_size / 2) + (merge_arr_size & 1);

    // Create new left half array
    int leftHalf[leftsize];
    for (int i = 0; i < leftsize; i++) {
        leftHalf[i] = merge_arr[i];
    }

    int rightHalf[rightsize];
    for (int i = 0; i < rightsize; i++) {
        rightHalf[i] = merge_arr[leftsize + i];
    }

    split(leftHalf, leftsize);
    split(rightHalf, rightsize);

    merge(merge_arr, leftHalf, leftsize, rightHalf, rightsize);

    // Print the left/right half array
    // for (int i = 0; i < leftsize; i++) {
    //     std::cout << leftHalf[i];
    //     if (i < leftsize - 1) {
    //         std::cout << ", "; 
    //     } 
    // }

    // std::cout << "\n"; 
    // std::cout << leftsize; 
    // std::cout << "\n"; 
    // std::cout << rightsize; 
    // std::cout << "\n"; 

    // for (int i = 0; i < rightsize; i++) {
    //     std::cout << rightHalf[i]; 
    //     if (i < rightsize - 1) {
    //         std::cout << ", "; 
    //     }
    // }

}

int main() {
    int user_merge_arr[] = {10, 20, 12, 13, 80, 32, 10};
    int merge_arr_size = sizeof(user_merge_arr) / sizeof(user_merge_arr[0]);

    split(user_merge_arr, merge_arr_size);

    std::cout << "Sorted Array: ";
    for (int i = 0; i < merge_arr_size; i++) {
        std::cout << user_merge_arr[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}


