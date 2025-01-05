#include <stdio.h>  

int main() {
    // How to declare an array
    int marks[5]; // declares an array of 5 integers

    // How to initialize an array
    int marks2[5] = {10, 20, 30, 40, 50}; // declares and initializes an array of 5 integers

    // How to access an array element
    int marks3[5] = {10, 20, 30, 40, 50};
    printf("\nFirst element of marks3: %d\n", marks3[0]); 
    // prints the first element of the array

    // How to modify an array element
    int marks4[5] = {10, 20, 30, 40, 50};
    marks4[0] = 100; // modifies the first element of the array
    printf("\nModified first element of marks4: %d\n", marks4[0]);

    // How to iterate over an array
    int marks5[5] = {10, 20, 30, 40, 50};
    printf("\nElements of marks5: ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", marks5[i]);
    }
    printf("\n\n");
    return 0;
}
o