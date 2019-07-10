# Take as input N, the size of array. Take N more inputs and store that in an array.
# Take N more inputs and store that in another array. Write a function which returns true if the second array is inverse of first and false otherwise. Print the value returned.

from TakeInputArray import Input
def ReverseCheck(arr1,arr2):
    flag = True
    Input(arr1)
    Input(arr2)
    for i in arr1:
        for j in range(len(arr2)-1,-1,-1):
            if i != arr2[j]:
                return False
            else:
                return True    
                       
# if __name__ == '___main__':    
array1 = []    
array2 = []    
print(ReverseCheck(array1,array2))
    