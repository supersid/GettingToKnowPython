# Take N(number in decimal format). Write a function that converts it to octal
# format. Print the value returned.

def DecimaltoOctal(decimal):
    rem,i,result=0,0,0
    while(decimal!=0):
        rem = decimal%8
        decimal = decimal//8
        result = result+(rem*pow(10,i))
        i=i+1
    return result
number = int(input("Enter Number:"))
print("Octal number for",number,"is",DecimaltoOctal(number))