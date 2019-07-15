# Take as input N, the size of array. Take N more inputs and store that in an array.
# Write a function that bubble sorts the array. Print the elements of sorted array.

from TakeInputArray import Input
from PrintArray import PrintArray
def BubbleSort(arr):
    Input(arr)
    n = len(arr)
    print("Orignal Array:",arr)
    for i in range(n):
        swap = False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swap = True
        if swap == False:
            break
    print("Sorted Array:",arr)

if __name__ == '__main__':    
    list=[]
    BubbleSort(list)
