import pdb
def DecimalToOctal(decimal):
    octal,q,r=0,0,0
    # pdb.set_trace()
    while(decimal!=0):
        q = decimal//8
        r = decimal%8
        decimal = q
        octal = octal*10 + r
    print(octal)
decimal = int(input("Enter Decimal Number:"))
DecimalToOctal(decimal)    
