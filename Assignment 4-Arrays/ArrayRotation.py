# --------------------ArrayRotation(one by one Method)--------------------------
def rotate(arr,d,n):
    for i in range (d):
        MainRotate(arr,n)

def MainRotate(arr,n):
    temp = arr[0]
    for i in range (n-1):
        arr[i] = arr[i+1]
    arr[n-1]=temp

def PrintArray(arr,n):
    for i in range(n):
        print(arr[i])

arr = [1,2,3,4,5]
rotate(arr,2,5)
PrintArray(arr,5)
