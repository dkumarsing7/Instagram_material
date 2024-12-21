#include <stdio.h>  

int main() {
    
    // Types of Arrays
    // 1. One-Dimensional Array:
    int arr[5] = {1, 2, 3, 4, 5};
    printf("First element of arr: %d\n", arr[0]);

    // 2. Two-Dimensional Array:
    int matrix[2][3] = {{1, 2, 3}, {4, 5, 6}};
    printf("Element at matrix[1][2]: %d\n", matrix[1][2]); // Prints 6

    // 3. Multi-Dimensional Array:
    // Arrays with more than two dimensions.
    int arr1[2][2][3] = {
        {{1, 2, 3}, {4, 5, 6}},
        {{7, 8, 9}, {10, 11, 12}}
    };
    printf("Element at arr1[1][1][2]: %d\n", arr1[1][1][2]); // Prints 12

    printf("\n");

    return 0;
}
