#include <stdio.h>  

int main() {
    
    // Common Operations
    // Traversing a one-dimensional array
    int arr[5] = {10, 20, 30, 40, 50};
    printf("element of arr: ");
    for(int i=0; i<sizeof(arr) / sizeof(arr[0]); i++){
        printf("%d ", arr[i]);
    }
    printf("\n");

    // Traversing a two-dimensional array
    int arr2[2][3] = {{10, 20}, {30, 40, 50}};
    printf("element of arr2: ");
    int row = sizeof(arr2) / sizeof(arr2[0]);
    int col = sizeof(arr2[0]) / sizeof(arr2[0][0]);

    for(int i=0; i<row; i++){
        for(int j=0; j<col; j++){
            printf("%d ", arr2[i][j]);
        };
    };
    printf("\n");

    return 0;
}
