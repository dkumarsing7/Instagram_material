#include <stdio.h>

void Selection_Sort(int size, int arr[])
{
    for (int j = 0; j < size-1; j++)
    {
        int min_ele = j;
        for (int i = j; i < size; i++)
        {
            if (arr[i] < arr[min_ele])
            {
                min_ele = i;
            }
        }
        int temp = arr[j];
        arr[j] = arr[min_ele];
        arr[min_ele] = temp;
    }
}

void print_arr(int size, int arr[])
{
    for (int i = 0; i < size; i++)
    {
        printf("%d ",arr[i]);
    }

}

int main()
{
    int arr[8] = {60, 10, 10, 20, 30, 80, 50, 20};
    int size = sizeof(arr) / sizeof(arr[0]);
    printf("original array is : \n");
    print_arr(size, arr);
    Selection_Sort(size, arr);
    printf("sorted array is : \n");
    print_arr(size, arr);
    return 0;
}
