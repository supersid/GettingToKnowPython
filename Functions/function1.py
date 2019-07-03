def BinaryToDecimal(n):
    decimal,i = 0,0
    while(n!=0):
        d = n%10
        decimal = decimal+(d*pow(2,i))
        n = n//10
        i = i+1
    print(decimal)

n = int(input("Enter Binary Number:"))
BinaryToDecimal(n)
