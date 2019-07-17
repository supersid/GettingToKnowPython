# Take as input N, the size of array. Take N more inputs and store that in an array.
# Write a function that selection sorts the array. Print the elements of sorted array.

def SelectionSort(arr):
    n = int(input("Enter Size of Array:"))
    for i in range(n):
        num = int(input("Enter {}st element of array:".format(i + 1)))
        arr.append(num)
    print("Initial Array:",arr)
    for i in range(0,len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[min_index]:
                print('true')
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    print("Sorted Array:",arr)
    
if __name__ == '__main__':
    list = []
    SelectionSort(list)
