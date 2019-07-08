# Take as input two numbers N1 and N2. Write a function which calculates and
# returns the LCM of two numbers. Print the value returned.

from function11 import gcd
def Lcm(number1,number2):
    return number1*number2/gcd(number1,number2)

num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))
print("LCM of",num1,"and",num2,"is",Lcm(num1,num2))