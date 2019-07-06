# -------Search an element in a sorted and rotated array----------

def search(arr, l, h, value):
    if(l>h):
        return -1
    
    mid = (l+h)//2
    if arr[mid] == value:
        return mid
    
    if arr[l] <= arr[mid]:
        
        if value >= arr[l] and value <= arr[mid]:
            return search(arr, l, mid-1, value)
        return search(arr, mid+1, h, value)
        
    else:
        if value <= arr[h] and value >= arr[mid]:
            return search(arr, mid+1, h, value)
        return search(arr, l, mid-1, value)
        
arr = [6,7,8,1,2,3,4,5]
value = 8
result = search(arr, 0, len(arr)-1, value)
if result != -1:
    print(result)
else:
    print('Value is not Present')        
