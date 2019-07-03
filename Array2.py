import pdb
def FindNum(n,m):
    list = []
    for i in range(n):
        num = int(input("Enter number"))
        list.append(num)
    # pdb.set_trace()
    x = False
    for j in range(len(list)):
        if list[j] == m:
            print("Index for",m,"is",j)
            x = True
    if x==False:
        print(-1)
n = int(input("Enter Size of Array"))
m = int(input("Enter the number to be found"))
FindNum(n,m)
