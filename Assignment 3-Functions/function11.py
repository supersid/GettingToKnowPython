# Take as input two numbers N1 and N2. Write a function which calculates and
# returns the GCD of two numbers. Print the value returned.
# I am using euclid algorithm.
def gcd(num1,num2):
    
    while(num2):
        num1,num2 = num2,num1%num2
    return num1

if __name__ == '__main__':
    number1 = int(input("Enter first number:"))
    number2 = int(input("Enter second number:"))
    print("GCD of",number1,"and",number2,"is",gcd(number1,number2))

