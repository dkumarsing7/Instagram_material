#include <stdio.h>  

int linear_Search(int search, int size, int arr[]){
    for (int i = 0; i < size; i++) {
        if(arr[i]==search) return i;
    }
    return -1;
}
int binary_Search(int search, int size, int arr[]){
    // In binary Search array should be sorted
    int low=0, high=size-1;
    while(low<=high){
        int mid=(low+high)/2;
        if(arr[mid]==search) return mid;
        else if(arr[mid]<search) low=mid+1;
        else high=mid-1;
    }    
    return -1;
}

int main() {
    int search = 40;    
    int arr[5] = {10, 20, 30, 40, 50};
    int size = sizeof(arr) / sizeof(arr[0]);
    // int index = linear_Search(search, size, arr);
    int index = binary_Search(search, size, arr);
    if(index != -1) printf("Element is present in array at index %d", index);
    else printf("Element is not present in array");
    return 0;
}
