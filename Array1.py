def MaxNum(n):
    list=[]
    for i in range(n):
        num = input("Enter number")
        list.append(num)
        max = list[0]
    for j in range(len(list)):
        if list[j]>max:
            max = list[j]
    print("Maximum Number is ",max)
        
n = int(input("Enter Size of Array"))
MaxNum(n)