#include <stdio.h>  

int main() {

    // Traversing a two-dimensional array
    int arr[2][3] = {{10, 20, 60}, {30, 40, 50}};
    
    int row = sizeof(arr) / sizeof(arr[0]);
    int col = sizeof(arr[0]) / sizeof(arr[0][0]);
    for(int i=0; i<row; i++){
        for(int j=0; j<col; j++){
            printf("%d ", arr[i][j]);
        }
    }

    return 0;
}
