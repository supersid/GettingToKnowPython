# Take as input N, the size of array. Take N more inputs and store that in an array.
# Write a function that reverses the array. Print the values in reversed array.
from TakeInputArray import Input
def Reverse(arr):
    rev = []
    Input(arr)
    for i in range(len(arr)-1,-1,-1):
        rev.append(arr[i])
    return rev
arr = []
print("Reverse of",arr,"is",Reverse(arr))