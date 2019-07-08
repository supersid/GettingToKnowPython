# Take as input two numbers N1 and N2.
# Write a function which prints first N1 terms of the series 3n + 2 which are not multiples of N2.

def Series(n1,n2):
    for i in  range(0,n1+1,1):
        a = (3*i)+2
        if a%n2==0:
            print(a)
            
if __name__ == '__main__':                            
    num1 = int(input("Enter Number of terms "))                
    num2 = int(input("Enter Number for divisibility check "))                
    Series(num1,num2)