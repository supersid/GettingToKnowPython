# Take as input two numbers x and n. 
# Write a function which calculates and returns the xn. Print the value returned.

def pow(x,n):
    i=2
    x2=x
    while(i<=n):
        x = x*x2
        i = i+1
    return x

if __name__ == '__main__':
    num = int(input("Enter Number :"))
    power = int(input("Enter Power"))
    print("{:d} raise to the power {:d} is".format(num, power),pow(num, power))
