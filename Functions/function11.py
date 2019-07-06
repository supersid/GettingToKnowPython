#gcd
def gcd(num1,num2):
    
    while(num2):
        num1,num2 = num2,num1%num2
    return num1
number1 = int(input("Enter first number:"))
number2 = int(input("Enter second number:"))
print("GCD of",number1,"and",number2,"is",gcd(number1,number2))

