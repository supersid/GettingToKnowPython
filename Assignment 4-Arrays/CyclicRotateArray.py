def Rotate(arr, n):
    temp  = arr[n-1]
    
    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]
    
    arr[0] = temp
    
arr = [1,2,3,4,5]
n = len(arr)

Rotate(arr, n)

for i in range(n):
    print(arr[i])
    
    