#this code will convert any base number to different base number
def SbToDb(ib,fb,number):
    result, rem, i = 0, 0, 0
#this converts any base to decimal
    while number!=0:
        rem = number%10
        number = number//10
        result =  result+(rem*pow(ib,i))
        i = i+1
    final=0
    i = 0
#this converts decimal to final base    
    while result!=0:
        rem = result%fb
        result = result//fb
        final = final+(rem*pow(10,i))
        i = i+1
    print(final)
ib = int(input("Enter Initial Base:"))
fb = int(input("Enter final Base:"))
number = int(input("Enter Number to be converted:"))
SbToDb(ib,fb,number)