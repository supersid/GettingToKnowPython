# Take as input a number N. Write a function which returns the integral part of
# square root of the number. Print the value returned.

def sqrt(num):
    num = num**0.5
    return num

n = float(input("Enter Number"))
print("Square root of {} is".format(n),sqrt(n))