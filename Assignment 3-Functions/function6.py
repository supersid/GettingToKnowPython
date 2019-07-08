# Take as input the following
# a. A number
# b. A digit
# Write a function that returns the number of times digit is found in the number.
# Print the value returned.
def DigitCounter(num,digit):
    counter = 0
    while(num>0):
        rem = num%10
        num = num//10
        if(rem == digit):
            counter = counter+1
    print("Number of times",digit,"occurs in",a,"is",counter)
    
    return(num>0)

if __name__ == '__main__':
    num = int(input("Enter Number:"))
    digit = int(input("Enter Digit to found:"))
    a = num
    DigitCounter(num,digit)
