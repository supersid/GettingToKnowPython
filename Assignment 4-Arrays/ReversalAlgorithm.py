# -------------------ArrayRotation(ReverseAlgorithm)----------------------------
def ReverseAlgorithm(arr,start,end):
    while(start<end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end]=temp
        start = start+1
        end = end-1

def Rotate(arr,d):
    n = len(arr)
    ReverseAlgorithm(arr,0,d-1)
    ReverseAlgorithm(arr,d,n-1)
    ReverseAlgorithm(arr,0,n-1)

def PrintArray(arr):
    for i in range (len(arr)):
        print(arr[i])

arr = [1,2,3,4,5]
Rotate(arr,2)
PrintArray(arr)
