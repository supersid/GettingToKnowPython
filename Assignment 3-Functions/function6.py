def DigitCounter(num,digit):
    counter = 0
    while(num>0):
        rem = num%10
        num = num//10
        if(rem == digit):
            counter = counter+1
    print("Number of times",digit,"occurs in",a,"is",counter)
    
    return(num>0)

num = int(input("Enter Number:"))
digit = int(input("Enter Digit to found:"))
a = num
DigitCounter(num,digit)